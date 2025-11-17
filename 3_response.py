def process_response(response):
    return (
        'HTTP/1.1 200 OK\r\n'
        f'Content-Length: {len(response)}\r\n'
        'Content-Type: text/html\r\n'
        '\r\n' +
        response +
        '\r\n'
    )