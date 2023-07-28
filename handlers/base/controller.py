from handlers.enums.http_status_code import HTTPStatusCode as StatusCode
from urllib.parse import urlparse, parse_qs
import json
import pandas as pd

class Controller():

    def __init__(self, web_handler=None) -> None:

        if web_handler:
            self.web_handler = web_handler

    def params(self):
        parsed_path = urlparse(self.web_handler.path)
        params = parse_qs(parsed_path.query)

        return {
            param: value[0] for param, value in params.items()
        } 

    def response(self, success=True, data=None, errors=None, status_code = StatusCode.OK.value, msg=None):
        self.web_handler.send_response(status_code) 
        self.web_handler.send_header('Content-Type', 'application/json') 
        self.web_handler.end_headers() 
        
        response = {
            "success": success
        }


        if data != None:
            response["data"] = data

        if msg != None:
            response["msg"] = msg

        if errors != None:
            response["success"] = False
            response["errors"] = errors

        return self.web_handler.wfile.write(json.dumps(response).encode()) 
    
  