class SimpleClientProtocol(WampClientProtocol):
    def __init__(self, *args, **kwargs):
        self.params = kwargs.pop('params', None)
        super(SimpleClientProtocol, self).__init__(*args, **kwargs)

    def show(self, result):
        print("SUCCESS:" + result)

    def logerror(self, e):
        erroruri, errodesc, errordetails = e.value.args
        print("ERROR: %s ('%s') - %s" % (erroruri, errodesc, errordetails))

    def done(self, *args):
        self.sendClose()
        reactor.stop()

    def onSessionOpen(self):
        if self.params:
            d1 = self.call("GenerateNonce", self.params).addCallback(self.show)
            # Puedes agregar más llamadas aquí con los parámetros que necesites
            DeferredList([d1]).addCallback(self.done)
        else:
            print("No se han proporcionado parámetros para llamar a onSessionOpen")


if __name__ == '__main__':
    log.startLogging(sys.stdout)
    # Cuenta 777774
    # factory = WampClientFactory("ws://91.223.152.18:8282", debugWamp = True)
    # factory = WampClientFactory("ws://10.25.0.1:3071", debugWamp = True)
    # factory = WampClientFactory("ws://186.46.0.180:3071", debugWamp = True)
    factory = WampClientFactory("ws://192.168.3.144:3081", debugWamp=True)
    params = "888"  # Parámetros que deseas enviar
    factory.protocol = SimpleClientProtocol
    connectWS(factory, params=params)  # Pasar los parámetros al conectar
    reactor.run()
