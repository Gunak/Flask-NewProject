"""Utilities for directory management."""

import os
import sys


# create a class called directoryManager
class DirectoryManager:
    """Utilities to create and manage files and folders."""

    def __init__(self, base_location=None):
        """base_location=None."""
    # set location to user specified location unless none was given,
    # then use current working directory
        if base_location is not None:
            self.base_location = base_location
        else:
            self.base_location = os.getcwd()

    def create_path(self, *AdditionalPath):
        """Take a base path and will append the AdditionalPath in order to create string of path desired."""
        # AdditionalPath creates a tuple of all options added
        slash = None
        if sys.platform.startswith("linux"):
            slash = "/"
        elif sys.platform.startswith("win32"):
            slash = "\\"

        for path in AdditionalPath:
            self.base_location = self.base_location + slash + path
        return self.base_location

    def create_dirs(self, path):
        directory = os.path.dirname(path)
        if not os.path.exists(path):
            os.mkdir(path)
