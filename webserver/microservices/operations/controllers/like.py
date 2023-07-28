import json
from typing import Any
from models.property import Property
from handlers.base.controller import Controller
from models.status import Status

class Like(Controller):


    def __init__(self, web_handler) -> None:
        self.route = "/like"
        self.name = "Like"
        self.method = "GET"
        self.web_handler = web_handler

    def __call__(self):
        
        result = {
            "success": True,
            "message": "Añadiendo like"
        }
        self.response(result)
         
