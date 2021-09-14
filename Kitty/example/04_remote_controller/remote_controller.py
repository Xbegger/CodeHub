from kitty.controllers import EmptyController
from kitty.remote.actor import RemoteActorServer

controller = EmptyController('Empty controller')
server = RemoteActorServer('127.0.0.1', 25002, controller)
server.start()
