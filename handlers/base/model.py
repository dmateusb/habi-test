from handlers.orm import ORM

class Model(ORM):

    hidden_attributes = []
    
    def __init__(self) -> None:
        pass

    def set__table_name(self, table_name):
        self._table_name = table_name

    def get_table_name(self):
        return self._table_name