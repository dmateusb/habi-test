from typing import Text
from enum import Enum

class Config(Enum):
    SERVICE_NAME: Text = "operations"
    SERVICE_PORT: int = 8001
    SERVICE_HOST: Text = "0.0.0.0"

    CONTROLLERS_FOLDER: Text = f"webserver.microservices.{SERVICE_NAME}.controllers"
