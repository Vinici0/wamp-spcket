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

```
class MessageHandler:
    @staticmethod
    def handle_message(protocol, payload):
        print("Received message:", payload)
        if payload == "GenerateNonce":
            protocol.call("GenerateNonce").addCallback(protocol.show)
        elif payload == "GetBalance":
            protocol.call("GetBalance").addCallback(protocol.show)
        elif payload == "GetDataVersion":
            protocol.call("GetDataVersion").addCallback(protocol.show)
        elif payload == "GetHelpText":
            protocol.call("GetHelpText").addCallback(protocol.show)
        elif payload == "GetImageText":
            protocol.call("GetImageText").addCallback(protocol.show)
        elif payload == "GetPanelState":
            protocol.call("GetPanelState", "panel_id", 1).addCallback(protocol.show)
        elif payload == "GetPanelGroups":
            protocol.call("GetPanelGroups").addCallback(protocol.show)
        elif payload == "GetEvents":
            protocol.call("GetEvents", "panel_id", 1, 0, 0, 1, False).addCallback(protocol.show)
        elif payload == "GetCurrentSubscriptions":
            protocol.call("GetCurrentSubscriptions", "panel_id", 1).addCallback(protocol.show)
        elif payload == "ChangePassword":
            protocol.call("ChangePassword", "login", "new_pass", "device_name").addCallback(protocol.show)
        elif payload == "SelectPanelEventsForNotify":
            protocol.call("SelectPanelEventsForNotify", "panel_id", 1, "1,2,3,4,7,8,9,14,...").addCallback(protocol.show)
        elif payload == "PushRegistration":
            protocol.call("PushRegistration", 0, "registration_id", "platform").addCallback(protocol.show)
        elif payload == "RemoteControl":
            protocol.call("RemoteControl", 10, "panel_id", 1, 0).addCallback(protocol.show)
        elif payload == "TechniqueOnPanel":
            protocol.call("TechniqueOnPanel", "panel_id", 20).addCallback(protocol.show)
        elif payload == "TechniqueLeftPanel":
            protocol.call("TechniqueLeftPanel", "panel_id").addCallback(protocol.show)
        elif payload == "ClearUserNotifications":
            protocol.call("ClearUserNotifications").addCallback(protocol.show)
        elif payload == "SetUserPreferences":
            protocol.call("SetUserPreferences", "notification_sound_file_name", 1).addCallback(protocol.show)
        elif payload == "CheckAlarmBtn":
            protocol.call("CheckAlarmBtn", "panel_id", 1, 31).addCallback(protocol.show)
        else:
            print("Unknown action:", payload)
    
    @staticmethod
    def saludo():
        print("Confirmando")

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
