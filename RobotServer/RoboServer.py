'''
Created on 19.06.2015

@author: mario
'''

#!/usr/bin/python

import json

from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

class BroadcastServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)

    def onMessage(self, msg, binary):
        for key, value in json.loads(msg).iteritems():
            if key == "X":
                if 0 <= value <= 180:
                    print "X: " + value
            if key == "Y":
                if 0 <= value <= 180:
                    print "Y: " + value

if __name__ == '__main__':
    import sys
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    ServerFactory = WebSocketServerFactory
    factory = ServerFactory("ws://localhost:9090")
    factory.protocol = BroadcastServerProtocol
    factory.setProtocolOptions(allowHixie76 = True)
    #listenWS(factory)
    reactor.listenTCP(9090, factory)
    reactor.run()
