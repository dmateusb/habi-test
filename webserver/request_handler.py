from http.server import BaseHTTPRequestHandler
from webserver.router import Router
from urllib.parse import urlparse, parse_qs
from handlers.logger import Logger
from handlers.enums.http_status_code import HTTPStatusCode
from handlers.base.controller import Controller

class RequestHandler(BaseHTTPRequestHandler):

    __logger = Logger(__name__)
    routes = {}
    
    def __init__(self, microservice, *args):
        self.microservice = microservice
        self.router = Router(self, microservice)
        self.routes = self.router.load_controllers()
        self.__controller_class = Controller(self)
        super().__init__(*args)


    def do_GET(self):
        parsed_path = urlparse(self.path)
        method = "GET"
        route = self.routes.get((method, parsed_path.path))

        if not route:
            return self.send_error(HTTPStatusCode.NOT_FOUND.value)
        try:
            return route()
        except Exception as e:
            self.__logger.print(str(e))
            msg = "Internal error server"
            self.__controller_class.response(
                msg=msg,
                success=False,
                status_code=HTTPStatusCode.SEVER_ERROR.value
            )