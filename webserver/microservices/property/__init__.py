from webserver.webserver import WebServer
from webserver.microservices.property.config import Config

class Service(WebServer):

    def __init__(self):
        super().__init__(
            host=Config.SERVICE_HOST.value,
            port=Config.SERVICE_PORT.value,
            name=Config.SERVICE_NAME.value
        )
        self.run()
