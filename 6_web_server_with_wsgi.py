import socket

def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split('')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )
    return  method, path, protocol, headers, body

def process_response(response):
    return (
        'HTTP/1.1 200 OK\r\n'
        f'Content-Length: {len(response)}\r\n'
        'Content-Type: text/html\r\n'
        '\r\n' +
        response +
        '\r\n'
    )

def to_environ(method, path, protocol, headers, body):
    return {
        'REQUEST_METHOD': method,
        'PATH_INFO': path,
        'SERVER_PROTOCOL': protocol,
        'wsgi.input': body,
        #**format_headers(headers)
        #...
    }

def start_response(status, headers):
    conn.sendall(f'HTTP/1.1 {status}\r\n')
    for (key, value) in headers:
        conn.sendall(f'{key}: {value}\r\n')
    conn.sendall('\r\n')

with socket.socket() as s:
    s.bind(('localhost', 8000))
    s.listen(1)
    conn,addr = s.accept()

    while True:
        with conn:
            http_request = conn.recv(1024).decode('utf-8')
            request = parse_http(http_request)
            environ = to_environ(*request)
            response = application(start_response, environ)  # Assuming 'application' is the WSGI application callable
            for data in response:
                conn.sendall(data.encode('utf-8'))