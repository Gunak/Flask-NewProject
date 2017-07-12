import os


# CLI - 
	# Create a new functional bluepring layout project
		# NewFunctional appName

		# Options
			# [--home]
	# Create a new view with template directory
		# NewFunctionalView viewName

class FunctionalBlueprint:
	"""Create a functional styple setup of a Flask Application."""

	# create the project directory
	def createProject(projectName, location=os.getcwd()):
		# create directory structure at current working directory unless specified
		pass

	def createNewView(name):
		# create a new file in views/ with name as {name}.py and directory in templates as {name}/
		pass