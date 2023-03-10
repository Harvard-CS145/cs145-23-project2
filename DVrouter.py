####################################################
# DVrouter.py
# Name:
#####################################################

import sys
from collections import defaultdict
from router import Router
from packet import Packet
from json import dumps, loads


class DVrouter(Router):
    """Distance vector routing protocol implementation."""

    def __init__(self, addr, heartbeatTime):
        """TODO: add your own class fields and initialization code here"""
        Router.__init__(self, addr)  # initialize superclass - don't remove
        self.heartbeatTime = heartbeatTime
        self.last_time = 0
        # Hints: initialize local state
        pass

    def handlePacket(self, port, packet):
        """TODO: process incoming packet"""
        if packet.isTraceroute():
            # Hints: this is a normal data packet
            # if the forwarding table contains packet.dstAddr
            #   send packet based on forwarding table, e.g., self.send(port, packet)
            pass
        else:
            # Hints: this is a routing packet generated by your routing protocol
            # if the received distance vector is different
            #   update the local copy of the distance vector
            #   update the distance vector of this router
            #   update the forwarding table
            #   broadcast the distance vector of this router to neighbors
            pass


    def handleNewLink(self, port, endpoint, cost):
        """TODO: handle new link"""
        # update the distance vector of this router
        # update the forwarding table
        # broadcast the distance vector of this router to neighbors
        pass


    def handleRemoveLink(self, port):
        """TODO: handle removed link"""
        # update the distance vector of this router
        # update the forwarding table
        # broadcast the distance vector of this router to neighbors
        pass


    def handleTime(self, timeMillisecs):
        """TODO: handle current time"""
        if timeMillisecs - self.last_time >= self.heartbeatTime:
            self.last_time = timeMillisecs
            # broadcast the distance vector of this router to neighbors
            pass


    def debugString(self):
        """TODO: generate a string for debugging in network visualizer"""
        return ""
