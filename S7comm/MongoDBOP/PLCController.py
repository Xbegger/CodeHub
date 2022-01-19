
from kitty.controllers.base import BaseController

class PLCController(BaseController):

    def __init__(self, name, logger=None, victim_alive_check_delay=0.3):
        super().__init__(name, logger=logger, victim_alive_check_delay=victim_alive_check_delay)

    def setPlug(self, plug):
        self.plug = plug

    # @Override
    def setup(self):
        self.plug.discover()
        pass

    # @Override
    def pre_test(self, test_number):
        return super().pre_test(test_number)


    # @Override
    def post_test(self):
        return super().post_test()