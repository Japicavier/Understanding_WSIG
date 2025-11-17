def to_environ(method, path, protocol, headers, body):
    return {
        'REQUEST_METHOD': method,
        'PATH_INFO': path,
        'SERVER_PROTOCOL': protocol,
        'wsgi.input': body,
        **format_headers(headers), #All headers have to be formatted, here is just an way to show it
        ...
    }
#The start response function has to be defined to be passed to the WSGI application
#This function is used by the application to start the HTTP response
#It also sends the status and headers to the client
def start_response(status, headers):
    conn.sendall(f'HTTP/1.1 {status}\r\n')
    for (key, value) in headers:
        conn.sendall(f'{key}: {value}\r\n')
    conn.sendall('\r\n')