# server.py

from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ("127.0.0.1", 4545)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()