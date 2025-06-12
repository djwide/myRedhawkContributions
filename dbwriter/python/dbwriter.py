'''
Author:
Cadet David Weidman USMA Class of 2016
321.297.9323
david.j.weidman2.mil@mail.mil
'''

from ossie.resource import start_component
import logging
import MySQLdb as mdb
import sys
from ossie.threadedcomponent import NOOP
from dbwriter_base import dbwriter_base


class dbwriter_i(dbwriter_base):
    """<DESCRIPTION GOES HERE>"""
    def initialize(self):
        """
        """
        dbwriter_base.initialize(self)
        self.count = 0
        print("connecting to db...")
        try:
            self.con = mdb.Connect('192.168.1.54', 'webserve', 'redhawk', 'RHtest')
            print("success")
            self.cursor = self.con.cursor()
        except mdb.Error as e:
            print("fail \n")
            print("Error {}: {}".format(e.args[0], e.args[1]))
            sys.exit(1)
        # TODO add customization here.

    def constructor(self):
        self.port_dataFloat_in.registerMessage("fromUpToInsert", dbwriter_base.FromUpToInsert, self.messageReceived)
        self.port_dataFloat_in2.registerMessage("fromCentToDB", dbwriter_base.FromCentToDB, self.messageReceived2)

    def process(self):

        return NOOP

    def messageReceived(self, msgId, msgData):
        '''self._log.info("messageReceived *************************")
        self._log.info("messageReceived msgId " + str(msgId))
        self._log.info("messageReceived msgData " + str(msgData))
        '''
        data = [msgData.X, msgData.Y]

        if data is None:
            return NOOP

        #YYYMMDDHHMMSS = datetime
        #f = open("rhtest.txt", "wr")
        insertString ='20160428094500, '+ '462.6325, '+ str(data[0]) + ", " +str(data[1])
        logging.info(insertString)
#        self.cursor.execute("INSERT INTO TestTable(time, dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, count) VALUES(" + insertString[0:len(insertString) - 3])
        self.cursor.execute("INSERT INTO target(time, frequency, latitude, longitude) VALUES(" + insertString +");")


    def messageReceived2(self, msgId, msgData):
        '''self._log.info("messageReceived *************************")
        self._log.info("messageReceived msgId " + str(msgId))
        self._log.info("messageReceived msgData " + str(msgData))
        '''
        tempLOB = msgData.aoa - msgData.comp
        #grab system time in the future.  must be in the data[0] format
        data = [
            '20170322104500',
            msgData.node,
            msgData.ave,
            msgData.freq,
            msgData.wave,
            msgData.lat,
            msgData.long,
            tempLOB,
        ]

        if data is None:
            return NOOP

        insertString= ""
        #YYYMMDDHHMMSS = datetime
        #f = open("rhtest.txt", "wr")
        for i in range(0, 7):
            insertString += str(data[i]) + ", "
        insertString += str(data[7])
        logging.info(insertString)
        self.cursor.execute("INSERT INTO receivers(time, sensorNum, db, frequency, wavelength, sensorlatitude, sensorlongitude, lob) VALUES(" + insertString +");")
#INSERT INTO TestTable(vals) VALUES(vals)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(dbwriter_i)
    print("test")
