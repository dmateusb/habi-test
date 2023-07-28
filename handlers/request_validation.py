from cerberus import Validator
from typing import Dict
from handlers.enums.http_status_code import HTTPStatusCode

class RequestValidation:
    document: Dict = {}    

    def __init__(self, params: Dict, status_fail: int=HTTPStatusCode.OK.value):
        self.params = params
        self.status_fail = status_fail
        self.validator = Validator(self.rules)

    def validate(self):
        self.validator.validate(self.params)
        errors = self.validator.errors

        if errors:
            return (errors, self.status_fail)