import socket
import subprocess
from sys import stderr
import time
from kitty.controllers.base import BaseController

class SessionServerController(BaseController):
    '''
    This controller controls our SessionServer.
    '''
    

    
    def __init__(self, name, host, port, logger=None):
        '''
        :param:
            name: name of the object
            host: Listen address for target
            port: Listen port fot target
            logger: Logger for the controller(default: None)
        
        :example:

            ::
                controller = ServerController(name='ServerController', host='target_ip', port=target_port)
        '''
        super(SessionServerController, self).__init__(name, logger)
        self._host = host
        self._port = port 
        self._server = None
        self._active = False


    def setup(self):
        super(SessionServerController, self).setup()
        self.logger.info('Trying to start target!!!')
        self._restart_target()
        if not self.is_victim_alive():
            msg = 'Controller cannot start target'
            raise Exception(msg)

    
    def teardown(self):
        super(SessionServerController, self).teardown()
        if not self.is_victim_alive():
            msg = 'Target is already down'
            self.logger.error(msg)
        else:
            msg = 'Test Finish'
            self.logger.info(msg)
    
    def post_test(self):
        super(SessionServerController, self).post_test()
        if not self.is_victim_alive():
            if self._server:
                out, err = self._server.communicate()
                self.logger.error(err)
                self.report.failed("Target does not respond")
                self. report.add('Traceback', err)
            else:
                self.logger.error("Target does not respond")
                self.report.failed("Target does not respond")
    
    def pre_test(self, test_number):
        self._restart_tartget()
        super(SessionServerController, self).pre_test(test_number)

    
    def _restart_target(self):
        '''
        Restart out Target
        '''
        if self._server:
            if self._server.returncode is None:
                self._server.kill()
                time.sleep(0.2)
        self._server = subprocess.Popen("python session_server.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


    def is_victim_alive(self):
        self._active = False

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((self.host, self.port))
            s.close()
            self._active = True
        except socket.error:
            return self._active
        return self._active

