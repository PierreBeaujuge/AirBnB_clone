#!/usr/bin/python3
"""
Unittest for the Amenity class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_amenity.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
# from models import base_model
from models import amenity
# from models.base_model import BaseModel
from models.amenity import Amenity
# from models import engine
# from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the Amenity class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        Amenity.name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the Amenity class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del Amenity.name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that State conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the Amenity methods are all present"""
        l1 = dir(Amenity)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the Amenity attributes are all present"""
        l1 = dir(Amenity)
        self.assertIn('name', l1)

    def test_instance_method_presence(self):
        """Test that the Amenity instance has the same methods"""
        l1 = dir(Amenity())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Test that the Amenity instance attributes are all present"""
        l1 = dir(Amenity())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('name', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(amenity.__doc__, None)
        self.assertIsNot(Amenity.__doc__, None)
        self.assertIsNot(Amenity.__init__.__doc__, None)
        self.assertIsNot(Amenity.save.__doc__, None)
        self.assertIsNot(Amenity.to_dict.__doc__, None)
        self.assertIsNot(Amenity.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'User()'"""

        am = Amenity()
        self.assertIsInstance(am, Amenity)
        self.assertIsInstance(am.id, str)
        self.assertIsInstance(am.created_at, datetime.datetime)
        self.assertIsInstance(am.updated_at, datetime.datetime)
        self.assertIsInstance(am.__class__, type)

        am.size = "tall"
        l1 = dir(am)
        self.assertIn('size', l1)
        self.assertEqual(am.__dict__['size'], 'tall')

        am.size = 'tall'
        l2 = dir(am)
        self.assertIn('size', l2)
        self.assertEqual(am.__dict__['size'], 'tall')

        am.age = 28
        l3 = dir(am)
        self.assertIn('age', l3)
        self.assertEqual(am.__dict__['age'], 28)

        am.age = 28.5
        l4 = dir(am)
        self.assertIn('age', l4)
        self.assertEqual(am.__dict__['age'], 28.5)

        am.age = None
        l5 = dir(am)
        self.assertIn('age', l5)
        self.assertEqual(am.__dict__['age'], None)

        am_kw1 = Amenity(**{})
        self.assertIsInstance(am_kw1, Amenity)
        self.assertIsInstance(am_kw1.id, str)
        self.assertIsInstance(am_kw1.created_at, datetime.datetime)
        self.assertIsInstance(am_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(am_kw1.__class__, type)

        am_kw2 = Amenity(**{"first_name": "John", "age": 25})
        l6 = dir(am_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(am_kw2.__dict__['first_name'], 'John')
        self.assertEqual(am_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        # storage = FileStorage()

        am = Amenity()
        temp = am.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        am.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(am.__dict__['updated_at'], temp)
        temp = am.__dict__['updated_at']
        # storage.reload()
        models.storage.reload()
        self.assertEqual(am.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        am = Amenity()
        am.age = 28
        am.size = "tall"
        for k, v in am.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, am.to_dict())
                self.assertEqual(v, am.to_dict()[k])
        self.assertEqual(am.to_dict()['__class__'], am.__class__.__name__)
        self.assertEqual(am.to_dict()['updated_at'], am.updated_at.isoformat())
        self.assertEqual(am.to_dict()['created_at'], am.created_at.isoformat())
        self.assertEqual(am.to_dict()['age'], 28)
        self.assertEqual(am.to_dict()['size'], 'tall')
        self.assertIsInstance(am.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        am = Amenity()
        string = '['+am.__class__.__name__+']'+' ('+am.id+') '+str(am.__dict__)
        self.assertEqual(string, am.__str__())
