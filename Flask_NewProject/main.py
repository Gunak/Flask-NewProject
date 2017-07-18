# Built-in imports
import argparse

# Packages imports
import blueprint
import structure
import script_info


def create():
	"""Ran to use the command line interface for Flask-NewProject.
	To create a new project
	FlaskNew <projectName> <directory> [options]

	Positional Arguments
		projectName 				This is the name of your project. This will name the project folderand package folder, if tnot the simple project
		directory 					This is the location that you what it to be created. Default is the current directory this is ran from. Else, specify full path.
		
	Options as follows:

		# Style setups
		--simple, -s 				this will create a very simple Flask project
		--simple-package, -S 		this will create a simple Flask project in a package format
		--functional, -f 			this will create the project as a Flask blueprint setup as a Functional style
		--divisional, -d 			this will create the project as a Flask blueprint setup as a Divisional style

		# Help options 				These options will only show how the directory and files will look, they will not be created.
		--help-simple				this will show how a simple setup would be created
		--help-simple-package		this will show how a simple package setup would be created
		--help-functional 			this will show how a Functional setup would be created
		--help-divisional	 		this will show how a Divisional setup would be created
		"""
    #parser = argparse.ArgumentParser()
    #parser.add_argument()

    pass


 def manage():
 	"""Manage a Flask project that is using Blueprints."""

 	pass