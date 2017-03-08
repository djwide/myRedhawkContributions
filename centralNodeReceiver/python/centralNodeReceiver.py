'''
Author: 
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
'''
from ossie.resource import start_component
import logging
import urllib
import re

from centralNodeReceiver_base import *
from MySQLdb.converters import Long2Int
#TODO
#Keep most current of each incoming node.  When all have changed/ enough time has passed send the requisite info to the updater
class centralNodeReceiver_i(centralNodeReceiver_base):
    """<DESCRIPTION GOES HERE>"""
    def constructor(self):
        self.port_message_in.registerMessage("accumMess", centralNodeReceiver_base.AccumMess, self.messageReceived)
        self.state= [False, True, True]#make all false in version where informaton is received from three sensors.
        #most recent readings
        self.ave1=.01
        self.ave2=.04
        self.ave3=.04
        self.aoa1= 5.0
        self.aoa2=6.0
        self.aoa3= 7.0
        self.compass1=0
        self.compass2=0
        self.compass3=0
        self.lob1=self.aoa1-self.compass1
        self.lob2=self.aoa2- self.compass2
        self.lob3=self.aoa3- self.compass3
        self.lat1= 41.39147
        self.lat2=41.39411
        self.lat3=41.39568
        self.long1=-73.95479
        self.long2=-73.95943 
        self.long3=-73.95592
        self.FREQ= 462.6375
    
    
    def messageReceived(self, msgId, msg):
        message= centralNodeReceiver_base.FromCentToUpdate()
        if(msg.nodeID==1):
            self.state[0]=True
            #we uploaded from a respberry pi to a webpage and pulled data off of the webpage bc we couldn't directly interface
            '''
            page= urllib.urlopen("http://192.168.1.200/")#very slow grabbing info from a rasPy
            fileStr= page.read()
            page.close()
            fileLis = re.split(',| |"', fileStr)
            #TODO make running average
            count= 0
            
            for x in fileLis:
                if fileLis[count]=="Latitude:":
                    self.lat1= fileLis[count+4]#second reading
                elif fileLis[count]=="\\nLongitude:":
                    self.long1= fileLis[count+4]
                elif fileLis[count]=="Headings:":
                    self.compass1= fileLis[count+4] 
                count= count+1
            '''
            self.ave1= msg.aveA
            self.lob1= msg.aoaA
            logging.info(msg.aveA)
            message2= centralNodeReceiver_base.FromCentToDB()
            message2.node=1
            message2.ave=self.ave1
            message2.lat= self.lat1
            message2.long= self.long1
            message2.freq= self.FREQ
            message2.wave= 300000000.0/(message2.freq*1000000)
            message2.aoa= self.aoa1
            message2.comp= self.compass1
            self.port_toDB.sendMessage(message2)
        if(msg.nodeID==2):
            self.state[1]=True
            '''
            page= urllib.urlopen("192.168.1.201")
            fileStr= page.read()
            page.close()
            fileLis = re.split(',| |"', fileStr)
            #TODO make running average
            logging.info(self.lat1)
            
            logging.info(fileLis)
            count= 0
            
            for x in fileLis:
                if fileLis[count]=="Latitude:":
                    logging.info("here")
                    self.lat2= fileLis[count+4]#second reading
                elif fileLis[count]=="Longitude:":
                    self.long2= fileLis[count+4]
                elif fileLis[count]=="Compass:":
                    self.compass1= fileLis[count+4] 
                count= count+1
            '''
            self.ave2= msg.aveA
            self.lob2= msg.aoaA
            
            message2= centralNodeReceiver_base.FromCentToDB()
            message2.node=2
            message2.ave=self.ave2
            message2.lat= self.lat2
            message2.long= self.long2
            message2.freq= self.FREQ
            message2.wave= 300000000.0/(message2.freq*1000000)
            message2.aoa= self.aoa2
            message2.comp= self.compass2
            self.port_toDB.sendMessage(message2)
        if(msg.nodeID==3):
            self.state[2]=True
            '''
            page= urllib.urlopen("192.168.1.202")
            fileStr= page.read()
            page.close()
            fileLis = re.split(',| |"', fileStr)
            #TODO make running average
            logging.info(self.lat1)
            
            logging.info(fileLis)
            count= 0
            
            for x in fileLis:
                if fileLis[count]=="Latitude:":
                    logging.info("here")
                    self.lat3= fileLis[count+4]#second reading
                elif fileLis[count]=="Longitude:":
                    self.long3= fileLis[count+4]
                elif fileLis[count]=="Compass:":
                    self.compass3= fileLis[count+4] 
                count= count+1
            '''
            self.ave3= msg.aveA
            self.lob3= msg.aoaA
            
            message2= centralNodeReceiver_base.FromCentToDB()
            message2.node=3
            message2.ave=self.ave3
            message2.lat= self.lat3
            message2.long= self.long3
            message2.freq= self.FREQ
            message2.wave= 300000000.0/(message2.freq*1000000)
            message2.aoa= self.aoa3
            message2.comp= self.compass3
            self.port_toDB.sendMessage(message2)
        
        if(self.state==[True,True,True]):
            message.aveUp1=self.ave1
            message.aveUp2=self.ave2
            message.aveUp3=self.ave3
            message.lobUp1=self.lob1
            message.lobUp2=self.lob2
            message.lobUp3=self.lob3
            message.lat1=self.lat1
            message.lat2=self.lat2
            message.lat3=self.lat3
            message.long1= self.long1
            message.long2= self.long2
            message.long3= self.long3          
            self.port_toUpdate.sendMessage(message)
            self.state= [False, True, True] #change to fff with three active nodes        
        
          
    def process(self):
        
        return NOOP

  
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(centralNodeReceiver_i)

