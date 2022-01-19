from re import template
import sys
import time
import traceback
import shlex
from binascii import hexlify
from threading import Event
import docopt
from kitty.fuzzers import test_list
from pkg_resources import get_distribution
from kitty.core import KittyException, KittyObject
from data_manager import DataManager, SessionInfo
from kitty.data.report import Report
from kitty.fuzzers.test_list import RangesList, StartEndList


class _Configuration(object):
    def __init__(self, delay_secs, store_all_reports, session_file_name, max_failures):
        self.delay_secs = delay_secs
        self.store_all_reports = store_all_reports
        self.session_file_name = session_file_name
        self.max_failures = max_failures

def _get_current_version():
    package_name = 'kittyfuzzer'
    current_version = get_distribution(package_name).version
    return current_version

class Fuzzer(KittyObject):
    '''
    
    '''

    def __init__(self, name='', logger=None, option_line=None):
        '''
        '''
        super(Fuzzer, self).__init__(name, logger)
        # session
        self.model = None
        self.dataman = None
        self.session_info = SessionInfo()
        self.config = _Configuration(
            delay_secs=0,
            store_all_reports=False,
            session_file_name=None,
            max_failures=None
        )
        # user interface
        self.user_interface = None
        #target
        self.target = None
        # event to implament pause / continue
        self._continue_event = Event()
        self._continue_event.set()

        self._fuzz_path = None
        self._fuzz_node = None
        self._last_payload = None
        self._skip_env_test = False
        self._in_environment_test = True
        self._started = False
        self._test_list = None
        self._handle_options(option_line)


    # handle options
    def _handle_options(self, option_line):
        '''
        Handle options from command line, in docopt style
        This allows passing arguments to the fuzzer from the command line
        without the need to re-write it in each runner

        :param option_line: string with the command line options to be parsed
        '''
        if option_line is not None:
            usage = '''
            There are the options to the kitty fuzzer object, not the options to the runner

            Usage:
                fuzzer [options] [-V ...]
            
            Options:
            -d --delay <delay>              delay between tests in seconds, float number
            -f --session <session-file>     session file name to use
            -n --no-env-test                don't perform environment test before the fuzzing 
            -r --retest <session-file>      retest failed/error tests from session file
            -t --test-list <test-list>      a comman delimted test list string of the form "-10,12,15-20,30-"
            -v --verbose                    be more verbose in the log
            '''
            options = docopt.docopt(usage, shlex.split(option_line))

            #ranges
            if options['--reset']:
                retest_file = options['--retest']
                try:
                    test_list_str = self.get_test_list_from_session_file(retest_file)
                except Exception as ex:
                    raise KittyException('Failed to open session file (%s) for retesting:%s' % (retest_file, ex))
            else:
                test_list_str = options['--test_list']
            self._set_test_ranges(None, None, test_list_str)

            #session file
            session_file = options['--session']
            if session_file is not None:
                self.set_session_file(session_file)
            
            #delay
            delay = options['--delay']
            if delay is not None:
                self.set_delay_between_tests(float(delay))
            
            #environment test
            skip_env_test = options['--no-env-test']
            if skip_env_test:
                self.set_skip_env_test(True)
            
            #verbosity
            verbosity = options['--verbose']
            self.set_verbosity(verbosity)

    @classmethod
    def get_test_list_from_session_file(session_file):
        dm = DataManager(session_file)
        dm.start()
        test_ids = dm.get_report_test_ids()
        if len(test_ids) == 0:
            raise KittyException('No failed tests in the session file %s' % session_file)
        test_list_str = ','.join('%s' % i for i in test_ids)
        dm.stop()
        return test_list_str

    def _set_test_ranges(self, start, end, test_list_str):
        '''
        test_list_str: 'x-y'
        '''
        if test_list_str and test_list_str.strip():
            self.set_test_list(test_list_str)
        else:
            s = 0 if start is None else int(start)
            e = end if end is None else int(end)
            self.set_range(s, e)
        
    def set_range(self, start_index=0, end_index=0):
        '''
        set range of tests to run
        '''
        if end_index is not None:
            end_index += 1
        self._test_list = StartEndList(start_index, end_index)
        self.session_info.start_index = start_index
        self.session_info.current_index = 0
        self.session_info.end_index = end_index
        self.session_info.test_list_str = self._test_list.as_test_list_str()
        # return self

    def set_test_list(self, test_list_str=''):
        '''
        :param test_list_str: listing of the test to execute

        The test list should be a comma-delimited string, and each element
        should be one of the following forms:

        '-x' - run from test 0 to test x
        'x-' - run from test x to the end
        'x' - run test x
        'x-y' - run from test x to test y

        To execute all tests, pass None or an empty string
        '''
        self.session_info.test_list_str = test_list_str
        self._test_list = RangesList(test_list_str)

    def set_session_file(self, filename):
        '''
        set session file name, 
        '''
        self.config.session_file_name = filename
        # return self
    
    def set_delay_between_tests(self, delay_secs):
        '''
        set duration between tests
        '''
        self.config.delay_secs = delay_secs
        # return self 

    def set_skip_env_test(self, skip_env_test=True):
        '''
        Set whether to skip the environment test
        '''
        self._skip_env_test = skip_env_test
    
    def set_store_all_reports(self, store_all_reports):
        self.config.store_all_reports = store_all_reports
        # return self


    # handle set target
    def set_target(self, target):
        '''
        set the target to fuzz
        '''
        self.target = target
        if target:
            self.target.set_fuzzer(self)
        return self
    
    # handle set session
    def set_model(self, model):
        self.model = model
        if self.model:
            self.model.set_notification_handler(self)
            self.handle_stage_changed(model)
        # return self

    def handle_stage_changed(self, model):
        '''
        handle a stage change in the data model
        '''
        stages = model.get_stages()
        if self.dataman:
            self.dataman.set('stages', stages)
        # return self

    def set_max_failures(self, max_failures):
        self.config.max_failures = max_failures
        # return self


    # handle set interface
    def set_interface(self, interface):
        self.user_interface = interface
        # return self

    
    def start(self):
        '''
        Start the fuzzing session

        If fuzzer already running, it will return immediatly
        '''
        if self._started:
            self.logger.warning("called while fuzzer is running. ignoring.")

        self._started = True
        assert(self.model)
        assert(self.user_interface)
        assert(self.target)
        assert(self.plug)
        assert(self.arpProxy)

        # init session_info
        if self._load_session():
            self._check_session_validity()
            self._set_test_ranges(
                self.session_info.start_index,
                self.session_info.end_index,
                self.session_info.test_list_str
            )
        else:
            self.session_info.kitty_version = _get_current_version()
            self.session_info.data_model_hash = self.model.hash()
        # init test list
        if self._test_list is None:
            self._test_list = StartEndList(0, self.model.num_mutations())
        else:
            self._test_list.set_last(self.model.last_index())
        
        # set session_info end_index
        list_count = self._test_list.get_count()
        self._test_list.skip(list_count - 1)
        self.session_info.end_index = self._test_list.current()
        ## back to the orignal state
        self._test_list.reset()
        self._test_list.skip(self.session_info.current_index)
        self._store_session()
        
        self.session_info.test_list_str = self._test_list.as_test_list_str()
        
        # set user_interface
        self._set_signal_handler()
        self.user_interface.set_data_provider(self.dataman)
        self.user_interface.set_continue_event(self._continue_event)
        self.user_interface.start()

        self.session_info.start_time = time.time()

        try:
            self._start_message()
            self.target.setup()
            start_from = self.session_info.current_index
            if self._skip_env_test:
                self.logger.info('Skipping environment test')
            else:
                self.logger.info('Performing environment test')
                self._test_environment()

            # reset test_llist ,bacuse of environment test
            self._test_list.reset()
            self._test_list.skip(start_from)
            self.session_info.current_index = start_from

            self.model.skip(self._test_list.current())
            self._start()
            return True

            
        except Exception as e:
            self.logger.error('Error occured while fuzzing: %s', repr(e))
            self.logger.error(traceback.format_exc())
            return False


    def _load_session(self):
        if not self.config.session_file_name:
            self.config.session_file_name = ':memory'
        self.dataman = DataManager(self.config.session_file_name)
        # why the dataman need start here
        self.dataman.start()
        if self.model:
            self.handle_stage_changed(self.model)
        self.dataman.set('log_file_name', self.get_log_file_name)
        info = self._get_session_info()
        if info:
            self.logger.info('Loaded session from DB')
            self.session_info = info
            return True
        self._set_session_info()
        return False
    
    def _get_session_info(self):
        info = self.dataman.get_session_info()
        return info
    
    def _set_session_info(self):
        self.dataman.set_session_info(self.session_info)
        self.dataman.set('fuzzer_name', self.get_name())
        self.dataman.set('session_file_name', self.config.session_file_name)

    def _check_session_validity(self):
        current_version = _get_current_version()
        if current_version != self.session_info.kitty_version:
            raise KittyException('kitty version in stored session (%s) != current kitty version (%s)' %(
                current_version,
                self.session_info.kitty_version
            ))
        model_hash = self.model.hash()
        if model_hash != self.session_info.data_model_hash:
            raise KittyException('data model hash in stored session(%s) != current data model hash(%s)' %(
                model_hash,
                self.session_info.data_model_hash
            ))

    def _store_session(self):
        self._set_session_info()

    def _set_signal_handler(self):
        import signal
        signal.signal(signal.SIGINT, self._exit_now)
    
    def _exit_now(self, dummy1, dummy2):
        self.stop()
        sys.exit(0)


    def _pre_test(self):
        self._update_test_info()
        self.session_info.current_index = self._test_list.current()
        self.target.pre_test(self.model.current_index())


    def _update_test_info(self):
        test_info = self.model.get_test_info()
        self.dataman.set('test_info', test_info)
        template_info = self.model.get_template_info()
        self.dataman.set('template_info', template_info)


    def _post_test(self):
        failure_detected = False
        self.target.post_test(self.model.current_index())
        report = self._get_report()
        status = report.get_status()
        if self._in_environment_test:
            return status != Report.PASSED    
        if status != Report.PASSED:
            self._store_report(report)
            self.user_interface.failuer_detected()
            failure_detected = True
            self.logger.warning('!! Failure detected !!')
        elif self.config.store_all_reports:
            self._store_report(report)
        
        if failure_detected:
            self.session_info.failure_count += 1
        self._store_session()

        if self.config.delay_secs:
            self.logger.debug('delaying for %f seconds', self.config.delay_secs)
            time.sleep(self.config.delay_secs)
        return failure_detected


    