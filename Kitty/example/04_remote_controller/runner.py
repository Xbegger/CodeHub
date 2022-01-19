from kitty import fuzzers
import six
from kitty.fuzzers import ServerFuzzer
from kitty.interfaces import WebInterface
from katnip.targets.file import FileTarget
from kitty.model import GraphModel
from kitty.model import String, Template
from kitty.remote.actor import RemoteActor


t1 = Template(name='T1', fields=[
    String('The default string', name='S1_1'),
])

'''Write content to files'''
##      Target
path = 'D:/CodeHub/Kitty/example/01_file_generator/tmp/'
target = FileTarget('FileTarget', path, 'fuzzed')

'''Connect to actual actor(controller) over RPC'''

controller = RemoteActor('127.0.0.1', 25002)

target.set_controller(controller)

##      Data Model
model = GraphModel()
model.connect(t1)

##      Fuzzer
fuzzer = ServerFuzzer(name='Example 4 - File Generator(Remote Controller')
fuzzer.set_interface(WebInterface(port=26001))
fuzzer.set_model(model)
fuzzer.set_target(target)

'''
No need for delay, we only create files
#fuzzer.set_delay_between_test(0.02)
No need for range, generator all
#fuzzer.set_range(50)
'''
fuzzer.start()
print('---------------------- done with fuzzing ---------------')
six.moves.input('press enter to exit')
fuzzer.stop()

