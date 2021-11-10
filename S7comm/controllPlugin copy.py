#-*-coding:utf8-*-

from MIPlugin import MIPlugin

ip = '192.168.137.190'
token = 'cf337484e9615f509fa39591bc802784'

plugin = MIPlugin(ip = ip, token = token)
# msg = {'did':'MYDID','siid':2,'piid':1,'value':False}
# msg = {'did':'MYDID',"siid": 2, "piid": 7}

# print(plugin.off())
print(plugin.off())

# recv = plugin.get_properties(msg)
# recv = plugin.set_properties([msg])
# recv = miioprotocol._

# plugin.off()
# print(recv)