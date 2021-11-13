#-*-coding:utf8-*-

from MIPlugin import MIPlugin

ip = '192.168.1.134'
token = '28aa291e4d034fe9a955d6e735153ae6'
plugin = MIPlugin(ip = ip, token = token)
# print(plugin.off())
print(plugin.on())



# msg = {'did':'MYDID','siid':2,'piid':1,'value':False}
# msg = {'did':'MYDID',"siid": 2, "piid": 7} 
# recv = plugin.get_properties(msg)
# recv = plugin.set_properties([msg])
# recv = miioprotocol._

# plugin.off()
# print(recv)