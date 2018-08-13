#hello.py

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return u'<h1>Hello, web!</h1>'.encode('utf8')
