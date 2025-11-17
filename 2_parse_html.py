def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split('')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )
    return  method, path, protocol, headers, body

'''
Este ejemplo de parsing sirve para un ejemplo sencillo de request de HTTTP
Sin embargo la forma en la que se hace un parsing de manera estándar es dividiendo los headers y el body por un doble salto.
De esa manera se evita el riesgo de que dentro del body haya saltos de línea que puedan crear headers incorrectos.

Ejemplo de un request que puede manejar este parser:
GET / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"

<body>Hello World</body>
'''