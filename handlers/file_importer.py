from importlib import import_module

class FileImporter:
	def __init__(self, file_name):
		self.file_name = import_module(file_name)

	def import_attribute(self, attr):
		return getattr(self.file_name, attr)

	def import_by_classname(self, classname):
		return self.import_attribute(classname)

	def import_by_functionname(self, function):
		return self.import_attribute(function)