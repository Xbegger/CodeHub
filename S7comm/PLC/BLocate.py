from struct import pack
from MyS7Client import MyS7Client
from BaseClass import Base

from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *



class BLocate(Base):

    def __init__(self, candidatePackets, handleCrush):
        super(BLocate, self).__init__()

        self.candidatePackets = candidatePackets
        self.__s7Client = handleCrush.getS7Client()
        self.__handleCrush = handleCrush


    def locate(self):
            
        candidatePackets = self.candidatePackets
        while(candidatePackets):
            chosenPackets, leftPackets, length = branchPackets(candidatePackets)

            msg = "chosenPacket from %d to %d ; leftPackets from %d to %d." %(0, length/2-1, length/2, length)
            self.logger.info(msg)
            for packet in chosenPackets:
                self.__s7Client.send_s7_packet(packet)
            crush = self.__s7Client.onlinePLC()
            if(crush == True):
                self.__handleCrush.handleCrush()
                if(isCurshPacket(chosenPackets) == True):
                    return chosenPackets
                else:
                    candidatePackets = chosenPackets
            else:
                if(isCurshPacket(leftPackets) == True):
                    return leftPackets
                else:
                    candidatePackets = leftPackets





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