'''
Usage:
    ./runner [--kitty-options=<kitty-options>]

Options:
    -k --kitty-options <kitty-options> options for the kitty fuzzer, use 6=--help to get a full list

This example stores the mutations in files under ./tmp/
It also demonstrate how to user kitty fuzzer command line options
'''

import docopt

from kitty import controllers
from kitty import fuzzers

from kitty.model import Template, String, Delimiter, ENC_INT_DEC, Dword, Static
from kitty.interfaces import WebInterface
from kitty.fuzzers import ServerFuzzer, server
from kitty.model import GraphModel
from kitty.targets.server import ServerTarget
from kitty.controllers import EmptyController
import socket
import six

opts = docopt.docopt(__doc__)

##      Data Model
http_get = Template(name='HTTP_GET', fields=[
    String('GET', name='method', fuzzable=False),
    Delimiter( ' ', name='space1', fuzzable=False),
    String('/index.html', name='path'),
    Delimiter(' ', name='space2'),
    String('HTTP', name='protocol name'),
    Delimiter('/', name='fws1'),
    Dword(1, name='major version', encoder=ENC_INT_DEC),
    Delimiter('.', name='dot1'),
    Dword(1, name='minor version', encoder=ENC_INT_DEC),
    Static('\r\n\r\n', name='eom')
])


##      Target
class TcpTarget(ServerTarget):
    def __init__(self, name, host, port, timeout=None, logger=None):
        super(TcpTarget, self).__init__(name, logger)
        self.host = host
        self.port = port
        if (host is None) or (port is None):
            raise ValueError('host and port may be None')

        self.timeout = timeout 
        self.socket = None
    
    
    def pre_test(self, test_num):
        super(TcpTarget, self).pre_test(test_num)

        if self.socket is None:
            sock = self._get_socket()
        if self.timeout is not None:
            sock.settimeout(self.timeout)

        sock.connect((self.host, self.port))

        self.socket = sock

    def _get_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def post_test(self, test_num):
        super(TcpTarget, self).post_test(test_num)
        if self.socket is not None:
            self.socket.close()
            self.socket = None


    def _send_to_target(self, data):
        self.socket.send(data)

    
    def _receive_from_target(self):
        return self.socket.recv(10000)

    
target = TcpTarget('target', 'localhost', 26010)

##      Controller
controller = EmptyController('EmptyController')

##      Target Load Controller
target.set_controller(controller)

##      Data Model
model = GraphModel()
model.connect(http_get)

##      Fuzzer
fuzzer = ServerFuzzer(name='Example 1 - File Generator', option_line=opts['--kitty-options'])
fuzzer.set_interface(WebInterface(port=26011))
fuzzer.set_model(model)
fuzzer.set_target(target)

fuzzer.start()

print('------------------------done with fuzzing------------')
six.moves.input('press enter to exit')
fuzzer.stop()
