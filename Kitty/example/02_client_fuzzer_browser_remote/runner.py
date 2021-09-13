import os
from kitty import controllers
from kitty.model import Template
from kitty.model import GraphModel
from kitty.fuzzers import ClientFuzzer
from kitty.interfaces import WebInterface
from katnip.controllers.client.process import ClientProcessController
from kitty.remote.rpc import RpcServer
from kitty.targets import ClientTarget
from kitty.remote import RpcClient

from katnip.legos.xml import XmlElement


def main():
    test_name = 'GET fuzzed'
    get_template = Template(name=test_name, fields=[
        XmlElement(name='html', element_name='head', content='<meta http-equiv="refresh" coontent="5; url=/">'),
        XmlElement(name='body', element_name='body', content='123', fuzz_content=True)
    ])

    fuzzer = ClientFuzzer(name='Example 2 - Browser Fuzzer (Remote)')
    fuzzer.set_interface(WebInterface(hosts='0.0.0.0'), port=26000)

    target = ClientTarget(name='BrowserTarget')

    '''
    Note: to avoid opening the process on our X server, we user another display for ite

    display ':2' that is specified below was started this way:
    >> sudo apt-get install xvfb
    >> Xvfb :2 -screen 2 1280x1024x8
    '''

    env = os.environ.copy()
    env['DISPLAY'] = ':2'
    controller = ClientProcessController(
        'BrowserController',
        'usr/bin/opera',
        ['http://localhost:8082/fuzzed'],
        process_env=env
    )

    target.set_controller(controller)
    target.set_mutation_server_timeout(20)

    ##      Data Model
    model = GraphModel()
    model.connect(get_template)

    ##      Fuzzer Set
    fuzzer.set_model(model)
    fuzzer.set_target(target)


    '''only fuzz the half of the mutations, just as an example'''
    fuzzer.set_range(end_index=model.num_mutations() // 2)
    fuzzer.set_delay_between_tests(0.1)

    remote = RpcServer(host='localhost', port=26007, impl=fuzzer)
    remote.start()

if __name__ == '__main__':
    main()

