from snap7 import client

#   实例化一个Client对象
my_plc = client.Client()


#   调用connect()方法

##      如果调用的时s7-200smart系列plc
##my_plc.set_connection_type(3)

##      如果连接的是logo！系列plc
##my_plc.set_connection_params(ip, local_tsap, remote_tsap)

'''
:param:
    ip: plcIP
    rack: 机架号
    slot: 卡槽号
:description:
    不同的plc对应不同的机架和卡槽，详情查表'''
my_plc.connect(ip, local_tsap, remote_tsap)

'''
:return:
    True:成功
    raise error: 报错'''
print(my_plc.get_connected())


#   断开连接
my_plc.disconnect()

##      plc实例不使用时，一定要销毁客户端
my_plc.destroy()



