import struct
from kitty.targets import ClientTarget
from kitty.controllers import ClientController
from kitty.interfaces import WebInterface
from kitty.fuzzers import ClientFuzzer
from kitty.model import GraphModel
from kitty.model import Template, Dynamic, String

 
#   Modified Stack
class MySpecialStack(object):
    def __init__(self):
        self.fuzzer = None
        self.names = {1:'Lumpy', 2:'Cuddles', 3:'Flaky', 4:'Petunya'}


    def set_fuzzer(self, fuzzer):
        self.fuzzer = fuzzer
    

    def handle_GetName(self, name_id):
        resp = self.fuzzer.get_mutation(stage='GetName response', data={
            'name_id':struct.pack('I', name_id)
        })
        if resp:
            return resp
        name = '' if name_id not in self.names else self.names[name_id]
        return struct.pack('I', name_id) + name




#   Data Model
get_name_response_template = Template(
    name='GetName response',
    fields=[
        Dynamic(key='name_id', default_value='\x00', name='name id'),
        String(value='admin', name='name')
    ]
)

#   controller Implementation
class MyClientController(ClientController):
    def __init__(self):
        super(MyClientController, self).__init__('MyClientController')

    
    def trigger(self):
        pass



#   Actual fuzzer code
##      Target:
###         target:ClientTarget 
###         name:Example Target
target = ClientTarget('Example Target')

##      Controller
###         含有触发器(trigger)的客户端控制器
controller = MyClientController()


##      为目标(Target)设置控制器
target.set_controller(controller)


model = GraphModel()
model.connect(get_name_response_template)

##      Fuzzer
###         客户端模糊器
###         装载Data Model、Target(included Controller)、Interface
fuzzer = ClientFuzzer()
fuzzer.set_model(model)
fuzzer.set_target(target)
fuzzer.set_interface(WebInterface())


##      启动客户端模糊测试
###         服务器栈
####            装载Fuzzer
my_stack = MySpecialStack()
my_stack.set_fuzzer(fuzzer)
fuzzer.start()
my_stack.start()