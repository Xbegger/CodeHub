from miio.miioprotocol import MiIOProtocol
from typing import Any


class MIPlugin():

    retry_count = 3
    timeout = 5
    def __init__(
        self,
        ip: str = None,
        token: str = None,
        start_id: int = 0,
        debug: int = 0,
        lazy_discover: bool = True,
        timeout: int = None,
    ) -> None:
        self.ip = ip
        self.token = token
        timeout = timeout if timeout is not None else self.timeout
        self._protocol = MiIOProtocol(
            ip, token, start_id, debug, lazy_discover, timeout
        )

    def discover(self):
        self._protocol.send_handshake()


    def send(
        self,
        command: str,
        parameters: Any = None,
        retry_count: int = None,
        *,
        extra_parameters=None,
    ) -> Any:
        """Send a command to the device.

        Basic format of the request:
        {"id": 1234, "method": command, "parameters": parameters}

        `extra_parameters` allows passing elements to the top-level of the request.
        This is necessary for some devices, such as gateway devices, which expect
        the sub-device identifier to be on the top-level.

        :param str command: Command to send
        :param dict parameters: Parameters to send
        :param int retry_count: How many times to retry on error
        :param dict extra_parameters: Extra top-level parameters
        """
        retry_count = retry_count if retry_count is not None else self.retry_count
        return self._protocol.send(
            command, parameters, retry_count, extra_parameters=extra_parameters
        )

    def on(self):
        """set the plugin on

            :return bool True: switch on the plugin sucess
            False: switch on the plugin failed
        """
        msg = {'did':'MYDID','siid':2,'piid':1,'value':True}
        recv = self.set_properties([msg])
        if self.power_status() == True:
            return True
        else:
            return False
    
    def off(self):
        """set the plugin off

            :return bool True: switch off the plugin sucess
                        False: switch off the plugin failed
        """
        msg = {'did':'MYDID','siid':2,'piid':1,'value':False}
        recv = self.set_properties([msg])
        if self.power_status() == False:
            return True
        else:
            return False


    def power_status(self):
        """get a status of plugin

            :return bool True: the plugin is on; 
                        False: the plugin is off;
        """
        msg = {'did':'MYDID','siid':2,'piid':1}
        recv = self.get_properties(msg)
        return recv[0]['value']

    def set_properties(self, parameters):
        """send a set_properties command

        :param dict parameters:Parameters to send
        """
        return self.send("set_properties", parameters)

    def get_properties(self, parameters):
        """send a get_properties command

        :param dict parameters:Parameters to send
        """
        return self.send("get_properties", [parameters])