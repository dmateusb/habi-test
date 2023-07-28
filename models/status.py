from handlers.base.model import Model
from typing import Text

class Status(Model):

    _table_name = "status"

    primary_key = "id"

    attributes = {
        "id": int,
        "name": Text,
        "label": Text
    }
