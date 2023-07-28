from typing import Text
from enum import Enum

class Config(Enum):
    SERVICE_NAME: Text = "property"
    SERVICE_PORT: int = 8000
    SERVICE_HOST: Text = "0.0.0.0"

    CONTROLLERS_FOLDER: Text = f"webserver.microservices.{SERVICE_NAME}.controllers"
