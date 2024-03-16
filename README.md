WebSocket Echo Server as Twisted Web Resource plus WSGI/Flask
=============================================================

This is a variant of a basic WebSocket Echo server that is running as a *Twisted Web Resource*.

Running
-------

Run the server by doing

    python server.py

and open

    http://localhost:8080/

in your browser.

This will show up all WebSocket messages exchanged between clients and server.

Link:
https://github.com/crossbario/autobahn-python/blob/master/docs/websocket/programming.rst


Example:

```
      function generateNonce(login) {
            const message = JSON.stringify({
                "method": "GenerateNonce",
                "login": login
            });
            sendMessage(message);
        }

        // Función para obtener el estado del panel
        function getPanelState(panelId, group) {
            const message = JSON.stringify({
                "method": "GetPanelState",
                "panelId": panelId,
                "group": group
            });
            sendMessage(message);
        }
```

Servidor
```
    def onMessage(self, payload, isBinary):
        # Manejar el mensaje recibido del cliente
        print("Mensaje recibido: ", payload)
        requestData = json.loads(payload.decode('utf8'))
        if requestData["method"] == "onSessionOpen":
            pass
        if requestData["method"] == "GetPanelState":
            print("ingreso a GetPanelState")
            d2 = self.call("GetPanelState", "777774", 2).addCallback(self.show)
            DeferredList([d2]).addCallback(self.done)
        print("Mensaje recibido: ", requestData)
```
