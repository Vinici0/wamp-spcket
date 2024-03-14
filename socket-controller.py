import sys
import json
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList
from autobahn.twisted.websocket import connectWS
from autobahn.wamp1.protocol import WampClientFactory, WampClientProtocol
from klein import Klein

app = Klein()

class SimpleClientProtocol(WampClientProtocol):
    array_events = []
    def __init__(self, nonce_value):
            self.nonce = None
            self.nonce_value = nonce_value

    def show(self, result):
        print("SUCCESS:" + result)

    def logerror(self, e):
        erroruri, errodesc, errordetails = e.value.args
        print("ERROR: %s ('%s') - %s" % (erroruri, errodesc, errordetails))

    def done(self, *args):
        self.sendClose()

    def onSessionOpen(self):
        d1 = self.call("GenerateNonce", self.nonce_value).addCallback(self.process_nonce).addErrback(self.logerror)
        self.array_events.append(d1)

    def process_nonce(self, result):
        self.nonce = result
        if self.nonce is not None:import sys
import json
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList
from autobahn.twisted.websocket import connectWS
from autobahn.wamp1.protocol import WampClientFactory, WampClientProtocol
from klein import Klein

app = Klein()

class SimpleClientProtocol(WampClientProtocol):
    array_events = []
    def __init__(self, nonce_value):
            self.nonce = None
            self.nonce_value = nonce_value

    def show(self, result):
        print("SUCCESS:" + result)

    def logerror(self, e):
        erroruri, errodesc, errordetails = e.value.args
        print("ERROR: %s ('%s') - %s" % (erroruri, errodesc, errordetails))

    def done(self, *args):
        self.sendClose()

    def onSessionOpen(self):
        d1 = self.call("GenerateNonce", self.nonce_value).addCallback(self.process_nonce).addErrback(self.logerror)
        self.array_events.append(d1)

    def process_nonce(self, result):
        self.nonce = result
        if self.nonce is not None:
            d2 = self.call("GetDataVersion").addCallback(self.show)
            self.array_events.append(d2)
            DeferredList(self.array_events).addCallback(self.done)

@app.route('/example/<nonce_value>', methods=['GET'])
def example_route(request, nonce_value):
    factory = WampClientFactory("ws://192.168.3.144:3081", debugWamp=True)
    factory.protocol = lambda: SimpleClientProtocol(nonce_value)
    connectWS(factory)
    return "OK"

@app.route('/saludo', methods=['POST'])
def saludo(request):
    content = json.loads(request.content.read())
    name = content['name']
    return f"Hola Mundo {name}"

if __name__ == '__main__':
    log.startLogging(sys.stdout)
    app.run('localhost', 8080)
            d2 = self.call("GetDataVersion").addCallback(self.show)
            self.array_events.append(d2)
            DeferredList(self.array_events).addCallback(self.done)

@app.route('/example/<nonce_value>', methods=['GET'])
def example_route(request, nonce_value):
    factory = WampClientFactory("ws://192.168.3.144:3081", debugWamp=True)
    factory.protocol = lambda: SimpleClientProtocol(nonce_value)
    connectWS(factory)
    return "OK"

if __name__ == '__main__':
    log.startLogging(sys.stdout)
    app.run('localhost', 8080)
