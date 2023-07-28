from enum import Enum

class HTTPStatusCode(Enum):
    OK = 200
    NOT_FOUND = 404
    SEVER_ERROR = 500