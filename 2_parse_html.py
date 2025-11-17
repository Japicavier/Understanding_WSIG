def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split('')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )
    return  method, path, protocol, headers, body

'''
This parsing example is for a simple HTTP request.
However, the standard way to parse is by splitting the headers and body with a double line break.
This avoids the risk of line breaks within the body that could create incorrect headers.

Example of a request that can handle this parser:
GET / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"

<body>Hello World</body>
'''