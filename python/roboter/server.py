#!/usr/bin/env python3
import http.server
import socket
import socketserver
import os
import pathlib
from subprocess import call

os.chdir(pathlib.Path(__file__).parent.resolve())
os.chdir("./public")
PORT = 4200

class WolkenWeltenHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        '''Reads post request body'''
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Done", "utf-8"))
        #httpd.server_close()
        #quit()

Handler = WolkenWeltenHandler
Handler.extensions_map={
	'.manifest': 'text/cache-manifest',
	'.html':     'text/html',
	'.png':      'image/png',
	'.jpg':      'image/jpg',
	'.svg':      'image/svg+xml',
	'.css':      'text/css',
	'.js':       'application/x-javascript',
	'.wasm':     'application/wasm',
	'':          'application/octet-stream'}


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("serving at port http://localhost:" + str(PORT))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()