from kitty.model import *



# an example of (pseudo) client hook
class StackImplementation:
    def build_get_response(self, request_id):
        resp = self.fuzzer.get_mutation(stage='get_response', 
                                        data={
                                            'request_id':request_id
                                        })
        if resp:
            return resp
        #build valid response
        resp = ''
        return resp
                