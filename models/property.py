from handlers.base.model import Model
from typing import Text

class Property(Model):
    
    _table_name = "property"

    hidden_attributes = [
        "id"
    ]

    primary_key = "id"
    
    foreign_attributes = [
        "status"
    ]

    attributes = {
        "id": int,
        "address": str,
        "city": str,
        "price": int,
        "description": str,
        "year": int
    }
         
        
