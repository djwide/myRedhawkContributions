'''
Author:
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
'''
from ossie.resource import start_component
import logging
from ossie.threadedcomponent import NOOP

from centralNodeReceiver_base import (
    centralNodeReceiver_base,
    FromCentToUpdate,
    FromCentToDB,
)

# TODO: Maintain the latest data from each node. When all nodes report, send
# the requisite information to the updater.


class centralNodeReceiver_i(centralNodeReceiver_base):
    """<DESCRIPTION GOES HERE>"""
    def constructor(self):
        self.port_message_in.registerMessage(
            "accumMess",
            centralNodeReceiver_base.AccumMess,
            self.messageReceived,
        )
        # Track whether updates have been received from each sensor. When data
        # arrives from all sensors this state will be reset.
        self.state = [False, True, True]
        # Most recent readings
        self.ave1 = 0.01
        self.ave2 = 0.04
        self.ave3 = 0.04
        self.aoa1 = 5.0
        self.aoa2 = 6.0
        self.aoa3 = 7.0
        self.compass1 = 0
        self.compass2 = 0
        self.compass3 = 0
        self.lob1 = self.aoa1 - self.compass1
        self.lob2 = self.aoa2 - self.compass2
        self.lob3 = self.aoa3 - self.compass3
        self.lat1 = 41.39147
        self.lat2 = 41.39411
        self.lat3 = 41.39568
        self.long1 = -73.95479
        self.long2 = -73.95943
        self.long3 = -73.95592
        self.FREQ = 462.6375

    def messageReceived(self, msgId, msg):
        message = FromCentToUpdate()
        if msg.nodeID == 1:
            self.state[0] = True
            # Uploaded from a Raspberry Pi to a webpage and pulled data from it
            # because a direct interface was unavailable
            self.ave1 = msg.aveA
            self.lob1 = msg.aoaA
            logging.info(msg.aveA)
            message2 = FromCentToDB()
            message2.node = 1
            message2.ave = self.ave1
            message2.lat = self.lat1
            message2.long = self.long1
            message2.freq = self.FREQ
            message2.wave = 300000000.0 / (message2.freq * 1000000)
            message2.aoa = self.aoa1
            message2.comp = self.compass1
            self.port_toDB.sendMessage(message2)
        if msg.nodeID == 2:
            self.state[1] = True
            self.ave2 = msg.aveA
            self.lob2 = msg.aoaA

            message2 = FromCentToDB()
            message2.node = 2
            message2.ave = self.ave2
            message2.lat = self.lat2
            message2.long = self.long2
            message2.freq = self.FREQ
            message2.wave = 300000000.0 / (message2.freq * 1000000)
            message2.aoa = self.aoa2
            message2.comp = self.compass2
            self.port_toDB.sendMessage(message2)
        if msg.nodeID == 3:
            self.state[2] = True
            self.ave3 = msg.aveA
            self.lob3 = msg.aoaA

            message2 = FromCentToDB()
            message2.node = 3
            message2.ave = self.ave3
            message2.lat = self.lat3
            message2.long = self.long3
            message2.freq = self.FREQ
            message2.wave = 300000000.0 / (message2.freq * 1000000)
            message2.aoa = self.aoa3
            message2.comp = self.compass3
            self.port_toDB.sendMessage(message2)

        if self.state == [True, True, True]:
            message.aveUp1 = self.ave1
            message.aveUp2 = self.ave2
            message.aveUp3 = self.ave3
            message.lobUp1 = self.lob1
            message.lobUp2 = self.lob2
            message.lobUp3 = self.lob3
            message.lat1 = self.lat1
            message.lat2 = self.lat2
            message.lat3 = self.lat3
            message.long1 = self.long1
            message.long2 = self.long2
            message.long3 = self.long3
            self.port_toUpdate.sendMessage(message)
            # Change to [False, False, False] when using three active nodes
            self.state = [False, True, True]

    def process(self):

        return NOOP


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(centralNodeReceiver_i)
