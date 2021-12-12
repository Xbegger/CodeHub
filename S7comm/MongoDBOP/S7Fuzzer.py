from kitty.fuzzers.base import BaseFuzzer

class S7Fuzzer(BaseFuzzer):
    '''
        S7Fuzzer is a class designed to fuzz S7 protocal PLC
        It does not create mutation

        contains three modules
            1. crush range locate
            2. target crush listen
            3. start binary positioning and get the ans 
    '''

    def __init__(self, name="S7Fuzzer", logger=None, option_line=None):
        '''
        :param name: name of the object
        :param logger: logger for the object (default: None)
        :param option_line: cmd line options to the fuzzer
        '''
        super(S7Fuzzer, self).__init__(name, logger, option_line)



    # @Override
    def _start(self):
        while True:
            sequence = self.model.get_sequence()
            try:
                self._run_sequence(sequence)
            except Exception as e:
                self.logger.error('Error occurred while fuzzing: %s', repr(e))
                self.logger.error(traceback.format_exc())
                break
    
    def _run_sequence(self, sequence):
        '''
        Run a single sequence
        '''
        self._check_pause()# _continue_event
        self._pre_test()#target.pre_test()
        session_data = self.target.get_session_data()
        self._test_info() 
        resp = None
        for edge in sequence:
            if edge.callback:
                edge.callback(self, edge, resp)
            session_data = self.target.get_session_data()
            node = edge.dst
            node.set_session_data(session_data)
            resp = self._transmit(node)
        return self._post_test()


    def _transmit(self, node):
        '''
        Transmit node data to target.

        :type node:  Template
        :param node: node to transmit
        :return: response if there is any
        '''
        payload = node.render().tobytes()
        self._last_payload = payload
        try:
            return self.target.transmit(payload)
        except Exception as e:
            self.logger.error('Error in transmit: %s', e)
            raise
