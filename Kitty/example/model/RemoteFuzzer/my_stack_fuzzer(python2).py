from kitty import controllers
from kitty.targets import ClientTarget
from kitty.controllers import ClientController
from kitty.interfaces import WebInterface
from kitty.fuzzers import ClientFuzzer
from kitty.model import GraphModel
from kitty.model import Template, Dynamic, String
from kitty.remote import RpcServer

#   Data Model
get_name_response_template = Template(
    name='GetName response',
    fields=[
        Dynamic(key='name_id', default_value='\x00',name='name id'),
        String(value='admin', name='name')
    ]
)

#   Controller
class MyClientController(ClientController):
    def __init__(self):
        super(MyClientController, self).__init__('MyClientController')
    
    def trigger(self):
        pass


#   Actual fuzzer Code
##      Target
target = ClientTarget('Example Target')

##      Controller
controller = MyClientController()

target.set_controller(controller)


##      Data Model
model = GraphModel()
model.connect(get_name_response_template)

##      Fuzzer
###         客户端模糊器
###         装载Data Model、Target、Interface
fuzzer = ClientFuzzer()
fuzzer.set_model(model)
fuzzer.set_target(target)
fuzzer.set_interface(WebInterface)


remote = RpcServer(host='127.0.0.1', port=26010, impl=fuzzer)
remote.start()

