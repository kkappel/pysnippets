#! /usr/bin/env python

# Our tutorial's WSGI server
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def application(environ, start_response):
   d = parse_qs(environ['QUERY_STRING'])
   url = d.get('url', [''])[0]
   url = d.get('url', [''])[0]
   url = d.get('url', [''])[0]
   url = d.get('url', [''])[0]


   # Always escape user input to avoid script injection
   age = escape(age)
   hobbies = [escape(hobby) for hobby in hobbies]

   # Sorting and stringifying the environment key, value pairs
   response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
   response_body = '\n'.join(response_body)

   status = '200 OK'
   response_headers = [('Content-Type', 'text/plain'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]



# Instantiate the WSGI server.
httpd = make_server('localhost', 8051, application)
#httpd.handle_request()
httpd.serve_forever()
