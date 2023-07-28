from http.server import HTTPServer
from webserver.request_handler import RequestHandler

class WebServer:
    
    def __init__(self, host, port, name) -> None:
        self.host = host
        self.port = port
        self.name = name
        self.server_class=HTTPServer

    def run(self, ):
        self.handler_class = self.handler
        server_address = (self.host, self.port)
        httpd = self.server_class(server_address, self.handler_class)
        print(f"Listeting on port: {self.port}...")
        httpd.serve_forever()

    def handler(self, *args):
        RequestHandler(self.name, *args)