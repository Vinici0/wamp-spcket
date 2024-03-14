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

    def __init__(self, *args, **kwargs):
        self.nonce = None
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def show(self, result):
        print("SUCCESS:" + result)

    def logerror(self, e):
        erroruri, errodesc, errordetails = e.value.args
        print("ERROR: %s ('%s') - %s" % (erroruri, errodesc, errordetails))

    def done(self, *args):
        self.sendClose()

    def onSessionOpen(self):
        d1 = self.call("GenerateNonce", "888").addCallback(self.process_nonce).addErrback(self.logerror)
        self.array_events.append(d1)

    def process_nonce(self, result):
        self.nonce = result
        if self.nonce is not None:
            d2 = self.call("GetDataVersion").addCallback(self.show)
            self.array_events.append(d2)
            # d3 = self.call("GetHelpText").addCallback(self.show)
            DeferredList(self.array_events).addCallback(self.done)

@app.route('/saludo', methods=['GET'])
def saludo(request):
    return 'Hola!'

@app.route('/example', methods=['GET'])  # Definimos los parámetros de la URL
def example_route(request):  # Recibimos los parámetros en la función de la ruta
    arg1 = "arg1"
    arg2 = "arg2"
    factory = WampClientFactory("ws://192.168.3.144:3081", debugWamp=True)
    factory.protocol = SimpleClientProtocol(arg1, arg2)
    connectWS(factory)
    return {
        "arg1": arg1,
        "arg2": arg2,
        "ok": True,
    }


@app.route('/get_data_version', methods=['POST'])
def get_data_version(request):
    data = request.content.read().decode('utf-8')
    data = json.loads(data)
    name = data['name']
    print(f"Name: {name}")
    return f"Name: {name}"

if __name__ == '__main__':
    log.startLogging(sys.stdout)
    app.run('localhost', 8080)
