#!/usr/bin/python3

import unittest
import pycodestyle
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)


class TestHBNBCommandPep8(unittest.TestCase):
    """ check for pycodestyle validation """
    def test_pycodestyle(self):
        """ test base for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(
                result.total_errors,
                0, "Found code style errors (and warning).")
