'''
Usage:
    ./runner [--kitty-options=<kitty-options>]

Options:
    -k --kitty-options <kitty-options> options for the kitty fuzzer, use --kitty-options=--help to get a full list

This example stores the mutations in files under ./tmp/
It also demonstrate how to user kitty fuzzer command line options
'''


import docopt
from katnip import targets
import six
from kitty.fuzzers import ServerFuzzer
from kitty.interfaces import WebInterface
from kitty.controllers import EmptyController
from katnip.targets.file import FileTarget
from kitty.model import GraphModel
from kitty.model import String
from kitty.model import Template

opts = docopt.docopt(__doc__)

t1 = Template(name='T1', fields=[
    String('The default string', name='S1_1'),
    String('Another string', name='S1_2'),
])

#   Writes content to files 

##      Target
path = './tmp'
target = FileTarget('FileTarget', path, 'fuzzed')
##      Controller
controller = EmptyController('EmptyController')
target.set_controller(controller)


##      Data Model
model = GraphModel()
model.connect(t1)

##      Fuzzer
fuzzer = ServerFuzzer(name='Example 1 - File Generator', option_line=opts['--kitty-options'])
fuzzer.set_interface(WebInterface(port=26001))
fuzzer.set_model(model)
fuzzer.set_target(target)
fuzzer.start()


print('------------------------done with fuzzing------------')
six.moves.input('press enter to exit')
fuzzer.stop()