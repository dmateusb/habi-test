from handlers.request_validation import RequestValidation
from handlers.enums.validations import Validations
from typing import Dict

class GetPropertiesValidation(RequestValidation):
    def __init__(self, document: Dict):
        super().__init__(document)

    @property
    def rules(self):
        return {
            "city": {
                "type": "string",
                "maxlength": 45,
                "required": False,
                "regex": Validations.ALPHA_SPACED.value
            },
            "status_id": {
                "type": "integer",
                "required": False,
                "coerce": int
            },
            "year": {
                "type": "integer",
                "required": False,
                "coerce": int,
                "min": 1900
            },
        }