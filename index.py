from handlers.cmd_args import HandleArgs
from handlers.file_importer import FileImporter

if __name__ == "__main__":
    args = HandleArgs.get_args()
    microservice = args.microservice
    microservice_folder = f"webserver.microservices.{microservice}"
    microservice = FileImporter(microservice_folder).import_by_classname("Service")
    microservice()
    