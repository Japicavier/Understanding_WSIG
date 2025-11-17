def application(environ, start_response):
    response = view(environ)
    start_response('200 OK', [
        ('Content-Length', len(response)),
    ])
    return [response]

def view(environ):
    path = environ['PATH_INFO']
    return f'Hello from {path}'


'''
In Django the creation of the application, or you could call it function, that wsig uses is in the line:
application = get_wsgi_application()
'''