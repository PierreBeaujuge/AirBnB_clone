#!/usr/bin/python3
"""
Unittest for the State class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_state.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
# from models import base_model
from models import state
# from models.base_model import BaseModel
from models.state import State
# from models import engine
# from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the State class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        State.name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Sets the public class attributes of the State class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del State.name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that State conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the State methods are all present"""
        l1 = dir(State)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the State attributes are all present"""
        l1 = dir(State)
        self.assertIn('name', l1)

    def test_instance_method_presence(self):
        """Test that the State instance has the same methods"""
        l1 = dir(State())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Test that the State instance attributes are all present"""
        l1 = dir(State())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('name', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(state.__doc__, None)
        self.assertIsNot(State.__doc__, None)
        self.assertIsNot(State.__init__.__doc__, None)
        self.assertIsNot(State.save.__doc__, None)
        self.assertIsNot(State.to_dict.__doc__, None)
        self.assertIsNot(State.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'User()'"""

        st = State()
        self.assertIsInstance(st, State)
        self.assertIsInstance(st.id, str)
        self.assertIsInstance(st.created_at, datetime.datetime)
        self.assertIsInstance(st.updated_at, datetime.datetime)
        self.assertIsInstance(st.__class__, type)

        st.size = "tall"
        l1 = dir(st)
        self.assertIn('size', l1)
        self.assertEqual(st.__dict__['size'], 'tall')

        st.size = 'tall'
        l2 = dir(st)
        self.assertIn('size', l2)
        self.assertEqual(st.__dict__['size'], 'tall')

        st.age = 28
        l3 = dir(st)
        self.assertIn('age', l3)
        self.assertEqual(st.__dict__['age'], 28)

        st.age = 28.5
        l4 = dir(st)
        self.assertIn('age', l4)
        self.assertEqual(st.__dict__['age'], 28.5)

        st.age = None
        l5 = dir(st)
        self.assertIn('age', l5)
        self.assertEqual(st.__dict__['age'], None)

        st_kw1 = State(**{})
        self.assertIsInstance(st_kw1, State)
        self.assertIsInstance(st_kw1.id, str)
        self.assertIsInstance(st_kw1.created_at, datetime.datetime)
        self.assertIsInstance(st_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(st_kw1.__class__, type)

        st_kw2 = State(**{"first_name": "John", "age": 25})
        l6 = dir(st_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(st_kw2.__dict__['first_name'], 'John')
        self.assertEqual(st_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        # storage = FileStorage()

        st = State()
        temp = st.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        st.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(st.__dict__['updated_at'], temp)
        temp = st.__dict__['updated_at']
        # storage.reload()
        models.storage.reload()
        self.assertEqual(st.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        st = State()
        st.age = 28
        st.size = "tall"
        for k, v in st.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, st.to_dict())
                self.assertEqual(v, st.to_dict()[k])
        self.assertEqual(st.to_dict()['__class__'], st.__class__.__name__)
        self.assertEqual(st.to_dict()['updated_at'], st.updated_at.isoformat())
        self.assertEqual(st.to_dict()['created_at'], st.created_at.isoformat())
        self.assertEqual(st.to_dict()['age'], 28)
        self.assertEqual(st.to_dict()['size'], 'tall')
        self.assertIsInstance(st.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        st = State()
        string = '['+st.__class__.__name__+']'+' ('+st.id+') '+str(st.__dict__)
        self.assertEqual(string, st.__str__())
