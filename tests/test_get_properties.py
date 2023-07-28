import unittest
from requests import request
from jsonschema import validate
from handlers.enums.http_status_code import HTTPStatusCode
import random
import string


class TestGetProperties(unittest.TestCase):

    cities = [
        "bogota",
        "medellin",
        "barranquilla",
        "manizales",
        "cali",
        "pereira",
        "dosquebradas",
        "belen de umbria",
        "bucaramanga",
        "la virginia",
        "Cartagena"
    ]

    status_descriptions = {
        "1": "Imueble en proceso de compra",
        "2": "Inmueble en propiedad de Habi",
        "3": "Inmueble publicado en preventa",
        "4": "Inmueble publicado en venta",
        "5": "Inmueble vendido",
    }

    hidden_statuses = [
        "1", "2", "3"
    ]

    def setUp(self) -> None:
        self.method = "GET"
        self.__URL_API = "http://0.0.0.0:8000/properties"

    def test_structure(self):
        self.send_request()
        self.assertEqual(self.response.status_code, HTTPStatusCode.OK.value)
        validate(self.response.json(), self.__successfull_schema())
        

    def test_wrong_params(self):
        params = {
            "city": self.__generate_random_characters(30),
            "year": self.__generate_random_characters(30),
            "status": self.__generate_random_characters(30)
        }
        self.send_request(params=params)
        validate(self.response.json(), self.__errors_schema())

    def test_filters(self):
        params = {}
        choosed_city = None
        choosed_year = None
        choosed_status_id = None

        if random.random() > 0.5:
            choosed_city = random.choice(self.cities)
            params["city"] = choosed_city

        if random.random() > 0.5:
            choosed_year = random.randint(2015, 2022)
            params["year"] = choosed_year

        if random.random() > 0.5:
            choosed_status_id = random.choice(list(self.status_descriptions))
            params["status_id"] = choosed_status_id

        self.send_request(params=params)

        for property in self.response.json()["data"]:
            if choosed_city:
                self.assertEqual(property.get("city"), choosed_city)
            if choosed_year:
                self.assertEqual(property.get("year"), choosed_year)
            if choosed_status_id:
                self.assertEqual(property.get(
                    "status"), self.status_descriptions.get(choosed_status_id))

    def test_not_hidden_statuses(self):
        hidden_statuses = [self.status_descriptions.get(
            hidden_status) for hidden_status in self.hidden_statuses]
        hidden_status = random.choice(self.hidden_statuses)
        params = {"status_id": hidden_status}
        self.send_request(params=params)
        data = self.response.json()["data"]
        hidden_status_on_reponse = list(
            filter(lambda x: x.get("status") in hidden_statuses, data))
        self.assertEqual(len(hidden_status_on_reponse), 0)

    def send_request(self, payload=None, params=None):

        self.response = request(
            method=self.method,
            url=self.__URL_API,
            data=payload,
            params=params
        )

    def __generate_random_characters(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def __successfull_schema(self):
        return {
            "definitions": {},
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": "https://example.com/object1690523277.json",
            "title": "Root",
            "type": "object",
            "required": [
                "success",
                "data"
            ],
            "properties": {
                "success": {
                    "$id": "#root/success",
                    "title": "Success",
                    "type": "boolean",
                    "examples": [
                            True
                    ],
                    "default": True
                },
                "data": {
                    "$id": "#root/data",
                    "title": "Data",
                    "type": "array",
                    "default": [],
                    "items": {
                            "$id": "#root/data/items",
                        "title": "Items",
                        "type": "object",
                                "required": [
                                    "address",
                                    "city",
                                    "status",
                                    "price",
                                    "description",
                                    "year"
                                ],
                            "properties": {
                                    "address": {
                                        "$id": "#root/data/items/address",
                                        "title": "address",
                                        "type": "string",
                                                "default": "",
                                                "examples": [
                                                    "calle 23 #45-67"
                                                ],
                                        "pattern": "^.*$"
                                    },
                                    "city": {
                                        "$id": "#root/data/items/city",
                                        "title": "city",
                                        "type": "string",
                                                "default": "",
                                                "examples": [
                                                    "medellin"
                                                ],
                                        "pattern": "^.*$"
                                    },
                                    "status": {
                                        "$id": "#root/data/items/status",
                                        "title": "status",
                                        "type": "string",
                                                "default": "",
                                                "examples": [
                                                    "Inmueble publicado en preventa"
                                                ],
                                        "pattern": "^.*$"
                                    },
                                    "price": {
                                        "$id": "#root/data/items/price",
                                        "title": "price",
                                        "type": "integer",
                                                "examples": [
                                                    210000000
                                                ],
                                        "default": 0
                                    },
                                    "description": {
                                        "$id": "#root/data/items/description",
                                        "title": "description",
                                        "type": ["string", "null"],
                                        "default": "",
                                        "examples": [
                                            ""
                                        ],
                                        "pattern": "^.*$"
                                    },
                                    "year": {
                                        "$id": "#root/data/items/year",
                                        "title": "year",
                                        "type": ["integer", "null"],
                                        "examples": [
                                            2002,
                                            ""
                                        ],
                                        "default": 0
                                    }
                                }
                    }

                }
            }
        }

    def __errors_schema(self):
        return {
            "definitions": {},
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": "https://example.com/object1690530006.json",
            "title": "Root",
            "type": "object",
            "required": [
                "success",
                "errors"
            ],
            "properties": {
                "success": {
                    "$id": "#root/success",
                    "title": "Success",
                    "type": "boolean",
                    "examples": [
                            False
                    ],
                    "default": True
                },
                "errors": {
                    "$id": "#root/errors",
                    "title": "Errors",
                    "type": "object",
                    "required": [
                        "city",
                        "status",
                        "year"
                    ],
                    "properties": {
                        "city": {
                            "$id": "#root/errors/city",
                            "title": "City",
                            "type": "array",
                            "default": [],
                            "items": {
                                "$id": "#root/errors/city/items",
                                "title": "Items",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "value does not match regex '^[a-zA-Z\\ ]*$'"
                                ],
                                "pattern": "^.*$"
                            }
                        },
                        "status": {
                            "$id": "#root/errors/status",
                            "title": "Status",
                            "type": "array",
                            "default": [],
                            "items": {
                                "$id": "#root/errors/status/items",
                                "title": "Items",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "unknown field"
                                ],
                                "pattern": "^.*$"
                            }
                        },
                        "year": {
                            "$id": "#root/errors/year",
                            "title": "Year",
                            "type": "array",
                            "default": [],
                            "items": {
                                "$id": "#root/errors/year/items",
                                "title": "Items",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "min value is 1900"
                                ],
                                "pattern": "^.*$"
                            }
                        }
                    }
                }

            }
        }


if __name__ == '__main__':
    unittest.main()
