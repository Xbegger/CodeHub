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
