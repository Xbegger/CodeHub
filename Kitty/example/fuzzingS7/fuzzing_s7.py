# coding:utf-8
from re import search
from kitty import fuzzers
from kitty.model import Template
from kitty.fuzzers import ServerFuzzer
from kitty.interfaces import WebInterface
from kitty.model import GraphModel
from katnip.targets.tcp import TcpTarget
from katnip.model.low_level.scapy import *
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
import binascii
from scapy import *
#   snap7 server 配置信息
target_ip = '192.168.178.21'
# target_ip = '127.0.0.1'
target_port = 102

randseed = int(RandShort())
#   COTP CR 请求的参数
SRC_TSAP = '\x01\x00'
DST_TSAP = '\x02\x00'


#   定义COTP CR 建立连接数据包
COTP_CR_PACKET = TPKT() / COTPCR()
COTP_CR_PACKET.Parameters = [COTPOption() for i in range(3)]
COTP_CR_PACKET.PDUType = "CR"
COTP_CR_PACKET.Parameters[0].ParameterCode = "tpdu-size"
COTP_CR_PACKET.Parameters[0].Parameter = "\x0a"
COTP_CR_PACKET.Parameters[1].ParameterCode = "src-tsap"
COTP_CR_PACKET.Parameters[2].ParameterCode = "dst-tsap"
COTP_CR_PACKET.Parameters[1].Parameter = SRC_TSAP
COTP_CR_PACKET.Parameters[2].Parameter = DST_TSAP


#   建立连接过程使用，fuzzable参数设置为False
COTP_CR_TEMPLATE = Template(name="cotp_cr", fields=[
    ScapyField(COTP_CR_PACKET, name="cotp_cr", fuzzable=False),
])

#   定义通讯参数配置数据结构
SETUP_COMM_PARAMETER_PACKET = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", Parameters=S7SetConParameter())

#   建立连接过程使用，fuzzable参数设置为False
SETUP_COMM_PARAMETER_TEMPLATE = Template(name='setup comm template', fields=[
    ScapyField(SETUP_COMM_PARAMETER_PACKET, name="setup comm", fuzzable=False)
])

#   定义需要Fuzzing的数据包结构，
READ_SZL_PACKET = TPKT() / COTPDT( EOT=1 ) / S7Header(ROSCTR="UserData",
                                                      Parameters=S7ReadSZLParameterReq(),
                                                      Data=S7ReadSZLDataReq(SZLId=RandShort(),
                                                                            SZLIndex=RandShort()))
#   定义READSZL_TEMPLATE为可以变异的结构，fuzzing的次数为1000
READ_SZL_TEMPLATE = Template(name="read szl template", fields=[
    ScapyField(READ_SZL_PACKET, name="read szl", fuzzable=True, fuzz_count=1000),
])

# payload = READ_SZL_TEMPLATE.render().tobytes().decode('unicode_escape')[2:-1].encode()
# payload = READ_SZL_TEMPLATE.render().tobytes().decode('unicode_escape')[2:-1].encode()
# print(type(payload))
# print(payload)
# # print(payload.decode('unicode_escape'))
# # print(payload.decode('unicode_escape').encode('latin1'))
# # print(payload.decode('unicode_escape').encode('latin1').decode('utf-8'))
# t = TPKT(payload)
# print(t.show())
# print(t.payload.load)
# t = COTPDT(t.payload.load)
# print(ls(t))
# print(t.payload.load)
# # t = S7Header(t.payload.load)
# # print(ls(t))
# # print("**************************")
# print(payload.hex())
# print(raw(READ_SZL_PACKET).hex())

    

#   使用GraphModel将数据包结构进行前后关联
#   使用GraphModel进行Fuzz
model = GraphModel()
##      在GraphModel中注册第一个节点，首先发送COTP_CR请求
model.connect(COTP_CR_TEMPLATE)
##      在GraphModel中注册第二个节点，在发送完COTP_CR后发送SETUP_PARAMETER请求
model.connect(COTP_CR_TEMPLATE, SETUP_COMM_PARAMETER_TEMPLATE)

##      早GraphModel中注册第三个节点，在发送完SETUP_COMM_PARAMETER_TEMPLATE后发送READ_SZL请求
model.connect(SETUP_COMM_PARAMETER_TEMPLATE, READ_SZL_TEMPLATE)


#   Target
s7comm_target = TcpTarget("s7comm target", host=target_ip, port=target_port, timeout=2)

#   定义是需要等待Target返回响应， 如果设置为True， Target不返回数据包就会被识别成异常进行记录
s7comm_target.set_expect_response(True)

#   Fuzzer
fuzzer = ServerFuzzer()

#   Interface
fuzzer.set_interface(WebInterface(port=26001))

#   在fuzzer中定义使用的Data Model
fuzzer.set_model(model)

#   在fuzzer中定义使用的Target
fuzzer.set_target(s7comm_target)

#   定义每个测试用例发送之间的延迟
fuzzer.set_delay_between_tests(0.1)

#   开始执行fuzz
fuzzer.start()

