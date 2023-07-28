import os
from handlers.file_importer import FileImporter

class Router:


    def __init__(self, web_handler, microservice) -> None:
        self.microservice = microservice    
        self.file_importer = FileImporter
        self.web_handler = web_handler
        self.load_controllers()

    def load_controllers(self):
        routes = {}
        controllers_folder_path = f"webserver/microservices/{self.microservice}/controllers"
        controllers_filepath = os.listdir(controllers_folder_path)
        controllers_filepath.remove("__pycache__")
        controllers_folder_path = controllers_folder_path.replace("/", ".")

        for controller_filepath in controllers_filepath:
            controller_filename = controller_filepath.replace(".py", "")
            controller_path = f"{controllers_folder_path}.{controller_filename}"
            controller_class_name = "".join([ x.capitalize() for x in controller_filename.split("_") ])
            controller = self.file_importer(controller_path).import_by_classname(controller_class_name)(self.web_handler)
            routes[ (controller.method, controller.route) ] = controller

        return routes
        

    