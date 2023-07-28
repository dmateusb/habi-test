from handlers.base.model import Model
from typing import Text

class StatusHistory(Model):

    _table_name = "status_history"

    hidden_attributes = [
        
    ]

    primary_key = "id"

    attributes = {
        "id": int,
        "property_id": Text,
        "status_id": int,
        "updated_date": Text
    }
