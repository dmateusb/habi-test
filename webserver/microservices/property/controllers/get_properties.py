import json
from typing import Any
from models.property import Property
from handlers.base.controller import Controller
from models.status import Status
from webserver.microservices.property.validations.get_properties_validation import GetPropertiesValidation
import pandas as pd

class GetProperties(Controller):

    ALLOWED_PROPERTY_STATUSES_NAMES = [
        "pre_venta",
        "en_venta",
        "vendido"
    ]

    filter_params = {
        "year": "=",
        "city": "=",
    }

    # table_name: (table_alias, backref, pk)
    foreign_filter_params = {
        "status": ("s", "status_id", "id", "=")
    }

    def __init__(self, web_handler) -> None:
        self.route = "/properties"
        self.name = "GerProperties"
        self.method = "GET"
        self.web_handler = web_handler

    def __call__(self):
        errors = GetPropertiesValidation(self.params()).validate()

        if errors:
            return self.response(
                errors=errors[0],
                status_code=errors[1]
            )
        
        self.__find_allowed_status_ids()
        select_query, from_query, join_queries, filters = self.__get_query_arguments()
        self.__set_request_params(filters)
        self.__set_request_foreign_params(filters)
        property = Property()
        property.set_select_query(select_query)
        property.set_from_query(from_query)
        property.set_joins(join_queries)
        property.set_filters(filters)
        result = property.all()
        data = self.__clean_data(result)
        self.response(data=data)

    def __find_allowed_status_ids(self):
        status = Status()
        allowed_statuses = "','".join(self.ALLOWED_PROPERTY_STATUSES_NAMES)
        status_filters = [
            ["name", "IN", f"('{allowed_statuses}')"]
        ]
        status.set_filters(status_filters)
        allowed_statuses = status.all()
        self.allowed_status_ids = "','".join(
            [str(status.get("id")) for status in allowed_statuses])
        
    def __set_request_params(self, filters):
        for param, operator in self.filter_params.items():
            if param in self.params():
                filters.append(
                    [param, operator, f"'{self.params().get(param)}'"])
                
    def __set_request_foreign_params(self, filters):
        for table, (alias, backref, pk, operator) in self.foreign_filter_params.items():
            if backref in self.params():
                filters.append([f"{alias}.{pk}", operator,
                               f"'{self.params().get(backref)}'"])

    def __get_query_arguments(self):
        select_query = "p.address AS address, p.city AS city, s.label AS status, p.price as price, p.description as Descripcion, p.year as year "
        from_query = "property p"
        join_queries = [
            ["JOIN", "status_history sh", [[
                "p.id", "=", "sh.property_id"]
            ]],

            ["JOIN", "status s", [
                ["sh.status_id", "=", "s.id"]
            ]],

            ["LEFT JOIN", "status_history sh2", [
                ["p.id", "=", "sh2.property_id"], [
                    "sh.update_date", "<", "sh2.update_date"]
            ]],
        ]
        filters = [
            ["sh2.id", "IS", "NULL"],
            ["s.id", "IN", f"('{self.allowed_status_ids}')"]
        ]
        return select_query, from_query, join_queries, filters
    
    def __clean_data(self, result = []):
        columns = Property().get_columns().split(",")
        columns.append("status")
        data_df = pd.DataFrame(result, columns=columns)
        data_df = data_df.fillna("")
        data_df["year"] = pd.to_numeric(data_df["year"], errors="coerce").astype("Int64")
        return data_df.to_dict("records")