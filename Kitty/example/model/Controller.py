from subprocess import PIPE
from kitty.controllers.base import BaseController
import os
import time

class LocalProcessController(BaseController):


    def __init__(self, name, process_path, process_args, logger=None):
        '''
        
        param:
            process_path: path to the targer executable
            process_args: arguments to pass to the process
            
        '''

        super(LocalProcessController, self).__init__(name, logger)
        assert(process_path)
        assert(os.path.exists(process_path))
        self._process_path = process_path
        self._process_name = os.path.basename(process_path)
        self._process_args = process_args
        self._process = None

    
    def pre_test(self, test_number):
        super(LocalProcessController, self).pre_test(test_number)

        # make sure process is ready for test
        if self._process:
            self._stop_process()
        
        cmd = [self._process_path] + self._process_args
        
        # start the process
        self._process = os.Popen(cmd, stdout=PIPE, stderr=PIPE)
        
        # add process information to the report
        self.report.add('process_name', self._process_name)
        self.report.add('process_path', self._process_path)
        self.report.add('process_args', self._process_args)
        self.report.add('process_id', self._process.pid)
        

    def post_test(self):

        self._stop_process()

        assert(self._process)

        # add process information to the report
        self.report.add('stdout', self._process.stdout.read())
        self.report.add('stderr', self._process.stderr.read())
        self.logger.debug('return code:%d', self._process.returncode)
        self.report.add('return_code', self._process.returncode)
        
        # if processs is crashed, have a differenr return code 
        if self._process.returncode != 0:
            self.report.failed('return code is not zero:%s' % self._process.returncode)
        
        self._process = None

        super(LocalProcessController, self).post_test()


    def teardown(self):
        self._stop_process()
        self._process = None
        super(LocalProcessController, self).teardown

    
    def _stop_process(self):
        if self._is_victim_alive():
            time.sleep(0.5)
            if self.is_victim_alive():
                self._process.kill()
                time.sleep(0.5)
                if self._is_victim_alive():
                    raise Exception('Failed to kill client process')
    
    def _is_victim_alive(self):
        #if process is create and process is not killed  return TRUE
        #Popen.poll()  None值表示进程尚未终止。
        return self._process and (self._process.poll() is None)