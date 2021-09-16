'''
        简单示例#1
    plc：   s7-1200
    变量地址:DB1.DBD36(1 是地址编号， 36 是起始值)
    类型    real(float)
'''

from snap7 import util,client
from snap7.types import S7AreaDB

#   实例化客户端
my_plc = client.Client()

#   连接s7-1200
my_plc.connect('192.168.2.1', 0, 0)

#   读出变量的字节数组
byte_arrays = my_plc.read_area(S7AreaDB, 1, 36, 4)

#   通过数据类型取值
value = util.get_real(byte_arrays, 0)

#断开连接
my_plc.disconnect

#   销毁
my_plc.destroy()

print(value)




'''
        简单示例#2
    plc:    s7-200SMART
    变量地址:M1.0(1 是起始值， 0 是bool索引)
    类型:   bool
'''
from snap7.types import S7AreaMK

#   实例化客户端
my_plc = client.Client()

#   设置连接资源类型
my_plc.set_connection_type(3)

#   连接s7-200SMART
my_plc.connect('192.168.2.2', 0, 1)

#   读出变量的字节数组
byte_arrays = my_plc.read_area(S7AreaMK, 0, 1, 1)

#   通过数据类型取值
value = util.get_bool(byte_arrays, 0, 0)

#   断开连接
my_plc.disconnect()

#   销毁
my_plc.destroy()

print(value)


'''
        示例
    plc:    s7-1200
    变量地址:[DB4, DBX0.1, DB4.DBD36, DB4.DBW2 ......]
    类型:   [bool, float, word ......]
'''




