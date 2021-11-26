from struct import pack
from MyS7Client import MyS7Client
from BaseClass import Base

from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *

import threading


class BLocate(Base):

    def __init__(self, candidatePackets, handleCrush):
        super(BLocate, self).__init__()

        self.candidatePackets = candidatePackets
        self.__s7Client = handleCrush.getS7Client()
        self.__handleCrush = handleCrush


    def locate(self):
        self.logger.info("Start binary search crush")
        candidatePackets = self.candidatePackets

        self.__s7Client.connect()
        # crushListenThread = threading.Thread(target=self.__s7Client.crushListen)
        # crushListenThread.start()
        self.__s7Client.crush.clear()
        while(candidatePackets):
            chosenPackets, leftPackets, length = branchPackets(candidatePackets)
            # add last test packet
            # chosenPackets.append(chosenPackets[0])

            # self.__s7Client.run.set()
            crush = False

            # self.__s7Client.crush = False
            msg = "chosenPacket from %d to %d ; leftPackets from %d to %d." %(0, length/2, length/2, length)
            self.logger.info(msg)
            
            for packet in chosenPackets:
                self.__s7Client.send_s7_packet(packet)
                time.sleep(5)
                if(self.__s7Client.crush.isSet() == True):
                    # 主动探测确认奔溃
                    crush = not self.__s7Client.onlinePLC()
                    if(crush == True):
                        # self.logger.info("find a crush")
                        break
                    else:
                        self.__s7Client.run.set()
    

            
            time.sleep(3)
            # crush = not self.__s7Client.onlinePLC()
            if(crush == True):
                self.logger.info("find a crush")
                self.__handleCrush.handleCrush()
                # time.sleep(3)
                self.__s7Client.connect()

                candidatePackets = chosenPackets
            else:
                candidatePackets = leftPackets

            if(isCurshPacket(candidatePackets) == True):
                break
        
        crushPacket = raw(candidatePackets[0]).hex()
        self.logger.info("Crush Packet is %s" % (crushPacket))
        return candidatePackets[0]
        







def branchPackets(candidatePackets):
    length = len(candidatePackets)
    half = length // 2
    chosenPackets = candidatePackets[0 : half]
    leftPackets = candidatePackets[half : ]
    return chosenPackets, leftPackets,length 



def isCurshPacket( packets):
    length = len(packets)
    if(length == 1):
        return True

    return False