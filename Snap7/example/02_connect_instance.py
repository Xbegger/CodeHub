from snap7 import client

def connect_logo(ip:str, local_tsap:int, remote_tsap:int, rack:int, slot:int):
    '''
    :function:
        连接logo系列
    :params:
        ip:    PLC/设备的IPV4地址
        local_tsap:    本地tasp(PC tsap)
        remote_tsap:    远程tsap(PLC tsap)
        rack:    服务器上的机架号
        slot:    服务器上的插槽
    :return:
        my_plc:    logo系列PLC
    '''
    #   初始化一个客户端
    my_plc = client.Client()
    #   设置内部(IP、 LocalTSAP、 RemoteTSAP)坐标。必须在connect()之前调用此函数
    my_plc.set_connection_params(ip, local_tsap, remote_tsap)
    #   连接到S7服务器
    my_plc.connect(ip, rack, slot)
    
    return my_plc


def connect_200smart(ip:str, plc_model=3, rack=0, slot=1):
    '''
    :function:
        连接s7-200smart系列
    :params:
        ip:    PLC/设备IPV4地址
        plc_model:    连接类型: 1 用于PG；2 用于OP， 3-10 用于S7基本
        rack:    服务器上的机架
        slot:    服务器上的插槽
    '''
    #   初始化一个客户端
    my_plc = client.Client()

    #   设置连接资源类型，即客户端， 连接到PLC
    my_plc.set_connection_type(plc_model)

    #   连接到S7服务器
    my_plc.connect(ip, rack, slot)

    return my_plc


def connect_plc(ip:str, rack:int, slot:int):
    '''
    :function:
        连接s7-1200/1500系列
    :params:
        ip:    PLC/设备的IPV4地址
        rack:    服务器上的机架
        slot:    服务器上的插槽
    '''
    my_plc = client.Client()
    my_plc.connect(ip, rack, slot)
    return my_plc