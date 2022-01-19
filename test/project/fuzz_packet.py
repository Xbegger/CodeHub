# coding=utf-8
import time
from MIPlugin import MIPlugin
from MyS7Client import MyS7Client
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.all import *
from arpcapture import *
import random
import pymongo
import datetime
target = MyS7Client(name="test", ip="192.168.1.188", src_ip="192.168.1.101", rack=0, slot=1)
m = RandTermString(RandNum(1, 20), '\x00')
n = raw(m).hex()
print(n)
print(type(n))
write_Packet = TPKT() / COTPDT(EOT=1) / S7Header(ProtocolId=0x32,
                                                 ROSCTR="Job", # S7comm协议
                                                 # ParameterLength=RandShort(),
                                                 # DataLength=RandShort(),
                                                 Parameters=S7WriteVarParameterReq(Function=0x05,#RandByte(), # 0x05写入
                                                                                   Items=S7WriteVarItemsReq(VariableSpecification=0x12,#RandByte(), #结构的主要类型 对于读/写消息，它总是具有值0x12，代表变量规范
                                                                                                            BlockNum=RandShort(),
                                                                                                            AREAType=RandEnumKeys(S7_AREA_TYPE),#RandByte(132), # 寻址变量的存储区域， 0x84为数据库 0x80为 Direct peripheral access
                                                                                                            BitAddress=RandShort()*RandByte() # 包含所选存储区中寻址变量的偏移量
                                                                                                            )
                                                                                   ),  # DB块号
                                                 Data=S7WriteVarDataItemsReq(ReturnCode=0x00,
                                                                             TransportSize=0x09,  # 0x07 Real access, len is in bytes
                                                                             Data=RandTermString(RandNum(1, 20), '\x00') # 随机生成数据，RandNum()随机指定长度 等价于random.randint(1,20)
                                                                             )
                                                 )  # 提交SNAP工作内容，发送出的数据包
READ_SZL_PACKET = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="UserData",
                                                    Parameters=S7ReadSZLParameterReq(),
                                                    Data=S7ReadSZLDataReq(SZLId=RandShort(),
                                                                          SZLIndex=RandShort()))
read_Packet = TPKT() / COTPDT( EOT=1 ) / S7Header(ROSCTR="Job",
                                                  Parameters=S7ReadVarParameterReq(Items=S7ReadVarItemsReq(TransportSize=RandEnumKeys(S7_TRANSPORT_SIZE_IN_PARM_ITEMS),
                                                                                                           GetLength=RandShort(),
                                                                                                           BlockNum=RandShort(),
                                                                                                           AREAType=RandEnumKeys(S7_AREA_TYPE),
                                                                                                           Address=RandShort()*RandByte()
                                                                                                          )))
# for i in range(10):
#   print(raw(write_Packet).hex())
# for i in range(10):
#   print(raw(read_Packet).hex())

print(raw(write_Packet).hex())


# print(target.get_transport_size_from_data_type('str'))