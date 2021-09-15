from kitty.remote import RpcClient
import struct

#   Modified Stack
class MySpecialStack(object):
    def __init__(self):
        self.fuzzer = None
        self.names = {
            1:'Lumpy',
            2:'Cuddles',
            3:'Flaky',
            4:'Petunya'
        }

    def set_fuzzer(self, fuzzer):
        self.fuzzer = fuzzer

    def handle_GetName(self, name_id):
        resp = self.fuzzer.get_mutation(stage='GetName response', data={
            'name_id':struct.pack('I',name_id)})
        
        if resp:
            return resp
        name = '' if name_id not in self.names else self.names[name_id]
        return struct.pack('I', name_id) + name
    
fuzzer = RpcClient(host='127.0.0.1', port=26010)

my_stack = MySpecialStack()
my_stack.set_fuzzer(fuzzer)

fuzzer.start()



