import json
from db.my_sql_connection import MySQLConnection
from mysql.connector import MySQLConnection as MySQLCon
import time


class ORM:

    filters = []
    select_query = None
    from_query = None
    join_queries = None
        
    @MySQLConnection()
    def all(
            self,
            order_by = None,
            sort="DESC",
            **kwargs
        ):
        connection: MySQLCon = kwargs.get("connection")
        self.create_initial_query()
        self.add_joins()
        self.add_where()
        self.add_order_by(order_by, sort)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(self.query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def create_initial_query(self):
        columns = self.get_columns()

        self.query = f"""
            SELECT {columns if not self.select_query else self.select_query}
            FROM {self.get_table_name() if not self.from_query else self.from_query}
        """
    
    def add_where(self):
        if self.filters:
            self.query += f" WHERE {self.filters}"
    
    def add_order_by(self, order_by, sort):
        if order_by:
            self.query += f" ORDER BY {order_by} {sort}"

    def add_joins(self):
        if self.join_queries:
            queries = []
            for join_query in self.join_queries:
                join_type = join_query[0]
                join_model = join_query[1]
                conditions = join_query[2]
                condition = self.set_filters(conditions, return_filter=True)
                query = f" {join_type} {join_model} ON {condition}"
                queries.append(query)

            self.query += " ".join(queries)    
            
    def get_columns(self):
        all_attributes = self.attributes.keys()
        attributes = list( set(all_attributes) - set(self.hidden_attributes) )
        return ",".join(attributes)
    
    def set_filters(self, filters, return_filter=False):
        conditions = []
        for filter in filters:
            attribute = filter[0]
            operator = filter[1]
            value = filter[2]
            condition = f"{attribute} {operator} {value}"
            conditions.append(condition)

        filters = " AND ".join(conditions)

        if not return_filter:
            self.filters = filters
            return self
        
        return filters
    
    def set_select_query(self, select_query):
        self.select_query = select_query
    
    def set_joins(self, join_queries):
        self.join_queries = join_queries
    
    def set_from_query(self, from_query):
        self.from_query = from_query