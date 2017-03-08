#!/usr/bin/env python
#
# AUTO-GENERATED CODE.  DO NOT MODIFY!
#
# Source: centralNodeReceiver.spd.xml
from ossie.cf import CF
from ossie.cf import CF__POA
from ossie.utils import uuid

from ossie.component import Component
from ossie.threadedcomponent import *
from ossie.properties import simple_property
from ossie.properties import simpleseq_property
from ossie.properties import struct_property

import Queue, copy, time, threading
from ossie.resource import usesport, providesport
from ossie.events import MessageConsumerPort
from ossie.events import MessageSupplierPort

class centralNodeReceiver_base(CF__POA.Resource, Component, ThreadedComponent):
        # These values can be altered in the __init__ of your derived class

        PAUSE = 0.0125 # The amount of time to sleep if process return NOOP
        TIMEOUT = 5.0 # The amount of time to wait for the process thread to die when stop() is called
        DEFAULT_QUEUE_SIZE = 100 # The number of BulkIO packets that can be in the queue before pushPacket will block

        def __init__(self, identifier, execparams):
            loggerName = (execparams['NAME_BINDING'].replace('/', '.')).rsplit("_", 1)[0]
            Component.__init__(self, identifier, execparams, loggerName=loggerName)
            ThreadedComponent.__init__(self)

            # self.auto_start is deprecated and is only kept for API compatibility
            # with 1.7.X and 1.8.0 components.  This variable may be removed
            # in future releases
            self.auto_start = False
            # Instantiate the default implementations for all ports on this component
            self.port_message_in = MessageConsumerPort(thread_sleep=0.1, parent = self)
            self.port_toUpdate = MessageSupplierPort()
            self.port_toDB = MessageSupplierPort()

        def start(self):
            Component.start(self)
            ThreadedComponent.startThread(self, pause=self.PAUSE)

        def stop(self):
            Component.stop(self)
            if not ThreadedComponent.stopThread(self, self.TIMEOUT):
                raise CF.Resource.StopError(CF.CF_NOTSET, "Processing thread did not die")

        def releaseObject(self):
            try:
                self.stop()
            except Exception:
                self._log.exception("Error stopping")
            Component.releaseObject(self)

        ######################################################################
        # PORTS
        # 
        # DO NOT ADD NEW PORTS HERE.  You can add ports in your derived class, in the SCD xml file, 
        # or via the IDE.

        port_message_in = providesport(name="message_in",
                                       repid="IDL:ExtendedEvent/MessageEvent:1.0",
                                       type_="control")

        port_toUpdate = usesport(name="toUpdate",
                                 repid="IDL:ExtendedEvent/MessageEvent:1.0",
                                 type_="control")

        port_toDB = usesport(name="toDB",
                             repid="IDL:ExtendedEvent/MessageEvent:1.0",
                             type_="control")

        ######################################################################
        # PROPERTIES
        # 
        # DO NOT ADD NEW PROPERTIES HERE.  You can add properties in your derived class, in the PRF xml file
        # or by using the IDE.
        class AccumMess(object):
            nodeID = simple_property(
                                     id_="nodeID",
                                     type_="octet")
        
            aveA = simple_property(
                                   id_="aveA",
                                   type_="float")
        
            wavelengthA = simple_property(
                                          id_="wavelengthA",
                                          type_="float")
        
            locLongA = simple_property(
                                       id_="locLongA",
                                       type_="float")
        
            locLatA = simple_property(
                                      id_="locLatA",
                                      type_="float")
        
            compassA = simple_property(
                                       id_="compassA",
                                       type_="float")
        
            aoaA = simple_property(
                                   id_="aoaA",
                                   type_="float")
        
            def __init__(self, **kw):
                """Construct an initialized instance of this struct definition"""
                for classattr in type(self).__dict__.itervalues():
                    if isinstance(classattr, (simple_property, simpleseq_property)):
                        classattr.initialize(self)
                for k,v in kw.items():
                    setattr(self,k,v)
        
            def __str__(self):
                """Return a string representation of this structure"""
                d = {}
                d["nodeID"] = self.nodeID
                d["aveA"] = self.aveA
                d["wavelengthA"] = self.wavelengthA
                d["locLongA"] = self.locLongA
                d["locLatA"] = self.locLatA
                d["compassA"] = self.compassA
                d["aoaA"] = self.aoaA
                return str(d)
        
            @classmethod
            def getId(cls):
                return "accumMess"
        
            @classmethod
            def isStruct(cls):
                return True
        
            def getMembers(self):
                return [("nodeID",self.nodeID),("aveA",self.aveA),("wavelengthA",self.wavelengthA),("locLongA",self.locLongA),("locLatA",self.locLatA),("compassA",self.compassA),("aoaA",self.aoaA)]
        
        accumMess = struct_property(id_="accumMess",
                                    structdef=AccumMess,
                                    configurationkind=("message",),
                                    mode="readwrite")
        
        class FromCentToUpdate(object):
            aveUp1 = simple_property(
                                     id_="aveUp1",
                                     type_="float")
        
            aveUp2 = simple_property(
                                     id_="aveUp2",
                                     type_="float")
        
            aveUp3 = simple_property(
                                     id_="aveUp3",
                                     type_="float")
        
            lobUp1 = simple_property(
                                     id_="lobUp1",
                                     type_="float")
        
            lobUp2 = simple_property(
                                     id_="lobUp2",
                                     type_="float")
        
            lobUp3 = simple_property(
                                     id_="lobUp3",
                                     type_="float")
        
            lat1 = simple_property(
                                   id_="lat1",
                                   type_="float")
        
            lat2 = simple_property(
                                   id_="lat2",
                                   type_="float")
        
            lat3 = simple_property(
                                   id_="lat3",
                                   type_="float")
        
            long1 = simple_property(
                                    id_="long1",
                                    type_="float")
        
            long2 = simple_property(
                                    id_="long2",
                                    type_="float")
        
            long3 = simple_property(
                                    id_="long3",
                                    type_="float")
        
            def __init__(self, **kw):
                """Construct an initialized instance of this struct definition"""
                for classattr in type(self).__dict__.itervalues():
                    if isinstance(classattr, (simple_property, simpleseq_property)):
                        classattr.initialize(self)
                for k,v in kw.items():
                    setattr(self,k,v)
        
            def __str__(self):
                """Return a string representation of this structure"""
                d = {}
                d["aveUp1"] = self.aveUp1
                d["aveUp2"] = self.aveUp2
                d["aveUp3"] = self.aveUp3
                d["lobUp1"] = self.lobUp1
                d["lobUp2"] = self.lobUp2
                d["lobUp3"] = self.lobUp3
                d["lat1"] = self.lat1
                d["lat2"] = self.lat2
                d["lat3"] = self.lat3
                d["long1"] = self.long1
                d["long2"] = self.long2
                d["long3"] = self.long3
                return str(d)
        
            @classmethod
            def getId(cls):
                return "fromCentToUpdate"
        
            @classmethod
            def isStruct(cls):
                return True
        
            def getMembers(self):
                return [("aveUp1",self.aveUp1),("aveUp2",self.aveUp2),("aveUp3",self.aveUp3),("lobUp1",self.lobUp1),("lobUp2",self.lobUp2),("lobUp3",self.lobUp3),("lat1",self.lat1),("lat2",self.lat2),("lat3",self.lat3),("long1",self.long1),("long2",self.long2),("long3",self.long3)]
        
        fromCentToUpdate = struct_property(id_="fromCentToUpdate",
                                           structdef=FromCentToUpdate,
                                           configurationkind=("message",),
                                           mode="readwrite")
        
        class FromCentToDB(object):
            ave = simple_property(
                                  id_="ave",
                                  type_="float")
        
            lat = simple_property(
                                  id_="lat",
                                  type_="float")
        
            long = simple_property(
                                   id_="long",
                                   type_="float")
        
            freq = simple_property(
                                   id_="freq",
                                   type_="float")
        
            aoa = simple_property(
                                  id_="aoa",
                                  type_="octet")
        
            node = simple_property(
                                   id_="node",
                                   type_="octet")
        
            wave = simple_property(
                                   id_="wave",
                                   type_="float")
        
            comp = simple_property(
                                   id_="comp",
                                   type_="octet")
        
            def __init__(self, **kw):
                """Construct an initialized instance of this struct definition"""
                for classattr in type(self).__dict__.itervalues():
                    if isinstance(classattr, (simple_property, simpleseq_property)):
                        classattr.initialize(self)
                for k,v in kw.items():
                    setattr(self,k,v)
        
            def __str__(self):
                """Return a string representation of this structure"""
                d = {}
                d["ave"] = self.ave
                d["lat"] = self.lat
                d["long"] = self.long
                d["freq"] = self.freq
                d["aoa"] = self.aoa
                d["node"] = self.node
                d["wave"] = self.wave
                d["comp"] = self.comp
                return str(d)
        
            @classmethod
            def getId(cls):
                return "fromCentToDB"
        
            @classmethod
            def isStruct(cls):
                return True
        
            def getMembers(self):
                return [("ave",self.ave),("lat",self.lat),("long",self.long),("freq",self.freq),("aoa",self.aoa),("node",self.node),("wave",self.wave),("comp",self.comp)]
        
        fromCentToDB = struct_property(id_="fromCentToDB",
                                       structdef=FromCentToDB,
                                       configurationkind=("property",),
                                       mode="readwrite")
        


