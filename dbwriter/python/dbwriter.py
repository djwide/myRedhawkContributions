"""Database writer component.

This module stores incoming measurements in a MySQL database.  It was
originally authored by Cadet David Weidman (USMA Class of 2016) and has
been updated for Python 3.
"""

from ossie.resource import start_component
import logging
import MySQLdb as mdb
import sys
from ossie.threadedcomponent import NOOP
from dbwriter_base import dbwriter_base


class dbwriter_i(dbwriter_base):
    """Insert received messages into the MySQL database."""
    def initialize(self):
        """Connect to the database and prepare the cursor."""
        dbwriter_base.initialize(self)
        self.count = 0
        print("connecting to db...")
        try:
            self.con = mdb.Connect(
                '192.168.1.54', 'webserve', 'redhawk', 'RHtest'
            )
            print("success")
            self.cursor = self.con.cursor()
        except mdb.Error as e:
            print("fail \n")
            print("Error {}: {}".format(e.args[0], e.args[1]))
            sys.exit(1)
        # TODO add customization here.

    def constructor(self):
        """Register incoming message ports."""
        self.port_dataFloat_in.registerMessage(
            "fromUpToInsert",
            dbwriter_base.FromUpToInsert,
            self.messageReceived,
        )
        self.port_dataFloat_in2.registerMessage(
            "fromCentToDB",
            dbwriter_base.FromCentToDB,
            self.messageReceived2,
        )

    def process(self):

        """Periodic processing hook; no asynchronous work required."""
        return NOOP

    def messageReceived(self, msgId, msgData):
        """Insert a simple X/Y data pair into the target table."""
        # self._log.info("messageReceived *************************")
        # self._log.info("messageReceived msgId " + str(msgId))
        # self._log.info("messageReceived msgData " + str(msgData))
        data = [msgData.X, msgData.Y]

        if data is None:
            return NOOP

        # YYYYMMDDHHMMSS = datetime
        # f = open("rhtest.txt", "wr")
        insertString = (
            f"20160428094500, 462.6325, {data[0]}, {data[1]}"
        )
        logging.info(insertString)
        # Example insert for a test table
        # self.cursor.execute(
        #     "INSERT INTO TestTable(time, dp1, dp2, dp3, dp4, dp5, dp6, dp7,"
        #     " dp8, dp9, dp10, count) VALUES("
        #     + insertString[0:len(insertString) - 3]
        # )
        self.cursor.execute(
            "INSERT INTO target(time, frequency, latitude, longitude) VALUES("
            + insertString
            + ");"
        )

    def messageReceived2(self, msgId, msgData):
        """Insert a record describing a sensor reading."""
        # self._log.info("messageReceived *************************")
        # self._log.info("messageReceived msgId " + str(msgId))
        # self._log.info("messageReceived msgData " + str(msgData))
        tempLOB = msgData.aoa - msgData.comp
        # Grab system time in the future; must be in the data[0] format
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

        insertString = ""
        # YYYYMMDDHHMMSS = datetime
        # f = open("rhtest.txt", "wr")
        for i in range(0, 7):
            insertString += str(data[i]) + ", "
        insertString += str(data[7])
        logging.info(insertString)
        self.cursor.execute(
            "INSERT INTO receivers(time, sensorNum, db, frequency, "
            "wavelength, sensorlatitude, sensorlongitude, lob) VALUES("
            + insertString
            + ");"

        )
# INSERT INTO TestTable(vals) VALUES(vals)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(dbwriter_i)
    print("test")
