# Conexión con el protocolo WAMP a IP:puerto

1. Obtener nonce (GenerateNonce)
2. Calcular hmac HmacSHA512, la clave es la contraseña del usuario, los datos son nonce+contraseña
3. Codificar hmac a base64
4. Registrarse (usar el valor del paso anterior como contraseña)
5. Ejecutar otro comando

## Registro

- `String login`
- `String pass`
- `String devicename` - Samsung SM-G9650, Xiaomi Mi 9T, etc.
- `String session_id` - opcional, identificador de sesión lógica obtenido del servidor con conexiones previas
- `int versionCode` - opcional, versión del protocolo que la aplicación admite
- `String appLocale` - opcional, idioma de la aplicación (por ejemplo, en, ru, etc.)
- `String osVersion` - opcional, versión del sistema operativo (Android 10, iOS 13.3.1, etc.)
- `String appVersion` - opcional, versión de la aplicación (3.0.0.28, 6.12, etc.)

## Informacion del Login
El código proporcionado es un ejemplo de cliente WebSocket que se conecta a un servidor WAMP (WebSocket Application Messaging Protocol) para realizar una serie de acciones. En particular, realiza un proceso de autenticación (registro) antes de ejecutar otros comandos.

Aquí hay un resumen del flujo de autenticación:

1. **GenerateNonce:** Este es el primer paso. El cliente solicita al servidor un nonce (un número que solo se usa una vez) asociado con el usuario. En este caso, el usuario es identificado por el login "888".

2. **Calculate hmac HmacSHA512:** Después de obtener el nonce, el cliente calcula un HMAC (Código de Autenticación de Mensajes Hash) utilizando SHA512. La clave para calcular el HMAC es la contraseña del usuario y los datos son el nonce concatenado con la contraseña.

3. **Signup:** El cliente envía la solicitud de registro al servidor, que incluye el login del usuario, el resultado del cálculo HMAC, el nombre del dispositivo, y opcionalmente otros detalles como la versión de la aplicación, el idioma, etc.

4. **Respuesta:** Si la solicitud de registro es exitosa, el servidor devuelve un conjunto de datos que incluye información sobre el usuario (como el rol, el IMEI del dispositivo, etc.), así como posiblemente otros detalles sobre el panel al que está conectado.

Después de este proceso de autenticación, el cliente puede ejecutar otros comandos en el servidor, como obtener el saldo, obtener la versión de los datos, obtener textos de ayuda, etc.

Esencialmente, el cliente establece una conexión WebSocket con el servidor, realiza el proceso de autenticación y luego puede interactuar con el servidor enviando y recibiendo mensajes según sea necesario.
