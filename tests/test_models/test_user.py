#!/usr/bin/python3
"""
Unittest for the User class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_user.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
# from models import base_model
from models import user
# from models.base_model import BaseModel
from models.user import User
# from models import engine
# from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the User class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the User class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del User.email
        del User.password
        del User.first_name
        del User.last_name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that User conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the User methods are all present"""
        l1 = dir(User)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the User attributes are all present"""
        l1 = dir(User)
        self.assertIn('email', l1)
        self.assertIn('password', l1)
        self.assertIn('first_name', l1)
        self.assertIn('last_name', l1)

    def test_instance_method_presence(self):
        """Test that the User instance has the same methods"""
        l1 = dir(User())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Test that the User instance attributes are all present"""
        l1 = dir(User())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('email', l1)
        self.assertIn('password', l1)
        self.assertIn('first_name', l1)
        self.assertIn('last_name', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(user.__doc__, None)
        self.assertIsNot(User.__doc__, None)
        self.assertIsNot(User.__init__.__doc__, None)
        self.assertIsNot(User.save.__doc__, None)
        self.assertIsNot(User.to_dict.__doc__, None)
        self.assertIsNot(User.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'User()'"""

        us = User()
        self.assertIsInstance(us, User)
        self.assertIsInstance(us.id, str)
        self.assertIsInstance(us.created_at, datetime.datetime)
        self.assertIsInstance(us.updated_at, datetime.datetime)
        self.assertIsInstance(us.__class__, type)

        us.size = "tall"
        l1 = dir(us)
        self.assertIn('size', l1)
        self.assertEqual(us.__dict__['size'], 'tall')

        us.size = 'tall'
        l2 = dir(us)
        self.assertIn('size', l2)
        self.assertEqual(us.__dict__['size'], 'tall')

        us.age = 28
        l3 = dir(us)
        self.assertIn('age', l3)
        self.assertEqual(us.__dict__['age'], 28)

        us.age = 28.5
        l4 = dir(us)
        self.assertIn('age', l4)
        self.assertEqual(us.__dict__['age'], 28.5)

        us.age = None
        l5 = dir(us)
        self.assertIn('age', l5)
        self.assertEqual(us.__dict__['age'], None)

        us_kw1 = User(**{})
        self.assertIsInstance(us_kw1, User)
        self.assertIsInstance(us_kw1.id, str)
        self.assertIsInstance(us_kw1.created_at, datetime.datetime)
        self.assertIsInstance(us_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(us_kw1.__class__, type)

        us_kw2 = User(**{"first_name": "John", "age": 25})
        l6 = dir(us_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(us_kw2.__dict__['first_name'], 'John')
        self.assertEqual(us_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        # storage = FileStorage()

        us = User()
        temp = us.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        us.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(us.__dict__['updated_at'], temp)
        temp = us.__dict__['updated_at']
        # storage.reload()
        models.storage.reload()
        self.assertEqual(us.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        us = User()
        us.age = 28
        us.size = "tall"
        for k, v in us.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, us.to_dict())
                self.assertEqual(v, us.to_dict()[k])
        self.assertEqual(us.to_dict()['__class__'], us.__class__.__name__)
        self.assertEqual(us.to_dict()['updated_at'], us.updated_at.isoformat())
        self.assertEqual(us.to_dict()['created_at'], us.created_at.isoformat())
        self.assertEqual(us.to_dict()['age'], 28)
        self.assertEqual(us.to_dict()['size'], 'tall')
        self.assertIsInstance(us.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        us = User()
        string = '['+us.__class__.__name__+']'+' ('+us.id+') '+str(us.__dict__)
        self.assertEqual(string, us.__str__())
