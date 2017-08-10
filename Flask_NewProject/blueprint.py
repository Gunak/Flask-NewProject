import os
from CreateDirs import create_dirs


class Blueprint:

	def __init__(self, projectName, location=None):
		self.projectName = projectName
		self.location = location

		self._PACKAGE_DIR = None
		self._PROJECT_DIR = None

		# what Functional and Divisional blueprints have in commpn
		# project name folder
		# in project folder:
			# __init__.py, models.py

	def create_package_folder(self):
		# create a directory with the same name as the project
		# check if location is default of None or if supplied by user
		if self.location != None:
			self.location = os.getcwd()
		

	def create_project_dir(self):
		# create directory structure at current working directory unless specified
		pass

	def create_init_fIle(self):
		# create __init__.py in project folder
		pass

	def create_models_file(self):
		# create models.py in project folder
		pass


class FunctionalBlueprint(Blueprint):
	"""Create a functional styple setup of a Flask Application."""
	def __init__(self,  projectName, location=None):
		super(Blueprint, self).__init__(projectName, location)

	def create_new_view(self, name):
		# create a new file in views/ with name as {name}.py
		pass

	def create_new_template(self, name):
		# create a new folder and html file as {name}

class DivisionalBlueprint(Blueprint):

	def __init__(self,  projectName, location):
		super().__init__(projectName, location)
