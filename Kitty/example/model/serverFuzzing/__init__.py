from subprocess import HIGH_PRIORITY_CLASS
from kitty.model import *

import TCPTarget
import Controller

# version 1
http_get_v1 = Template( name='HTTP_GET_V1', fields=[
    String( 'Get', name='method'),
    Delimiter( ' ', name='space1'),
    String( '/index.html', name='path'),
    Delimiter( ' ', name='space2'),
    String( 'HTTP/1.1', name='protocol'),
    Delimiter( '\r\n\r\n', name='eom'),
])

# version 2
http_get_v2 = Template( name='HTTP_GET_V2', fields=[
    String('GET', name='method'),
    Delimiter(' ', name='space1'),
    String('/index.html', name='path'),
    Delimiter(' ', name='space2'),
    String('HTTP', name='protocol name'),
    Delimiter('/', name='fws1'),
    Dword(1, name='major version', encoder=ENC_INT_DEC),
    Delimiter('.', name='dot1'),
    Dword(1, name='minor version', encoder=ENC_INT_DEC),
    Delimiter('\r\n\r\n', name='eom')
])

# version 3
http_get_v3 = Template(name='HTTP_GET_V3', fields=[
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


#Target
##setup()
target_name = 'test_target'
host = 'localhost'
port = 8080
timeout = 10000
pre_test_num = 5
post_test_num = 5
target = TCPTarget.TcpTarget(target_name, host, port)
##pre_test(test_num)
target.pre_test(pre_test_num)
##transmit
data = ''
target._send_to_target(data)
receiveData = target._receive_from_target()
##post_test(test_num)
target.post_test(post_test_num)
##get_report()
report_target = target.report

#Controller
##setup()
controller_name = 'test_controller'
process_path = ''
process_args = ''
controller = Controller.LocalProcessController(controller_name)
##pre_test(test_number)
controller_test_number = 5

controller.pre_test(controller_test_number)
##post_test()
controller.post_test()
##get_report()
report_controller = controller.report
##teardown()
controller.teardown()















