#!/usr/bin/python3
"""
Unittest for the BaseModel class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import base_model
from models.base_model import BaseModel
# from models import engine
# from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Method called immediately after the test method has been called and
        the result recorded
        """
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that BaseModel conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the BaseModel methods are all present"""
        l1 = dir(BaseModel)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_method_presence(self):
        """Test that the BaseModel instance has the same methods"""
        l1 = dir(BaseModel())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Test that the BaseModel instance attributes are all present"""
        l1 = dir(BaseModel())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(base_model.__doc__, None)
        self.assertIsNot(BaseModel.__init__.__doc__, None)
        self.assertIsNot(BaseModel.save.__doc__, None)
        self.assertIsNot(BaseModel.to_dict.__doc__, None)
        self.assertIsNot(BaseModel.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'BaseModel()'"""

        ba = BaseModel()
        self.assertIsInstance(ba, BaseModel)
        self.assertIsInstance(ba.id, str)
        self.assertIsInstance(ba.created_at, datetime.datetime)
        self.assertIsInstance(ba.updated_at, datetime.datetime)
        self.assertIsInstance(ba.__class__, type)

        ba.size = "tall"
        l1 = dir(ba)
        self.assertIn('size', l1)
        self.assertEqual(ba.__dict__['size'], 'tall')

        ba.size = 'tall'
        l2 = dir(ba)
        self.assertIn('size', l2)
        self.assertEqual(ba.__dict__['size'], 'tall')

        ba.age = 28
        l3 = dir(ba)
        self.assertIn('age', l3)
        self.assertEqual(ba.__dict__['age'], 28)

        ba.age = 28.5
        l4 = dir(ba)
        self.assertIn('age', l4)
        self.assertEqual(ba.__dict__['age'], 28.5)

        ba.age = None
        l5 = dir(ba)
        self.assertIn('age', l5)
        self.assertEqual(ba.__dict__['age'], None)

        ba_kw1 = BaseModel(**{})
        self.assertIsInstance(ba_kw1, BaseModel)
        self.assertIsInstance(ba_kw1.id, str)
        self.assertIsInstance(ba_kw1.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw1.__class__, type)

        ba_kw2 = BaseModel(**{"first_name": "John"})
        l6 = dir(ba_kw2)
        self.assertIn('first_name', l6)
        self.assertEqual(ba_kw2.__dict__['first_name'], 'John')
        # self.assertIsInstance(ba_kw2.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw2.updated_at, datetime.datetime)

        ba_kw3 = BaseModel(**{"first_name": 'John'})
        l7 = dir(ba_kw3)
        self.assertIn('first_name', l7)
        self.assertEqual(ba_kw3.__dict__['first_name'], 'John')
        # self.assertIsInstance(ba_kw3.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw3.updated_at, datetime.datetime)

        ba_kw4 = BaseModel(**{"age": 28})
        l8 = dir(ba_kw4)
        self.assertIn('age', l8)
        self.assertEqual(ba_kw4.__dict__['age'], 28)
        # self.assertIsInstance(ba_kw4.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw4.updated_at, datetime.datetime)

        ba_kw5 = BaseModel(**{"age": 28.5})
        l9 = dir(ba_kw5)
        self.assertIn('age', l9)
        self.assertEqual(ba_kw5.__dict__['age'], 28.5)
        # self.assertIsInstance(ba_kw5.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw5.updated_at, datetime.datetime)

        ba_kw6 = BaseModel(**{"age": None})
        l10 = dir(ba_kw6)
        self.assertIn('age', l10)
        self.assertEqual(ba_kw6.__dict__['age'], None)
        # self.assertIsInstance(ba_kw6.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw6.updated_at, datetime.datetime)

        ba_kw7 = BaseModel(**{"age": float('inf')})
        l11 = dir(ba_kw7)
        self.assertIn('age', l11)
        self.assertEqual(ba_kw7.__dict__['age'], float('inf'))
        # self.assertIsInstance(ba_kw7.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw7.updated_at, datetime.datetime)

        # ba_kw8 = BaseModel(**{"age": float('nan')})
        # l12 = dir(ba_kw8)
        # self.assertIn('age', l12)
        # self.assertEqual(ba_kw8.__dict__['age'], float('nan'))
        # self.assertIsInstance(ba_kw8.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw8.updated_at, datetime.datetime)

        ba_kw9 = BaseModel(**{"first_name": "John", "last_name": "Smith"})
        l13 = dir(ba_kw9)
        self.assertIn('first_name', l13)
        self.assertIn('last_name', l13)
        self.assertEqual(ba_kw9.__dict__['first_name'], 'John')
        self.assertEqual(ba_kw9.__dict__['last_name'], 'Smith')
        # self.assertIsInstance(ba_kw9.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw9.updated_at, datetime.datetime)

        ba_kw11 = BaseModel({})
        self.assertIsInstance(ba_kw11, BaseModel)
        self.assertIsInstance(ba_kw11.id, str)
        self.assertIsInstance(ba_kw11.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw11.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw11.__class__, type)

        ba_kw12 = BaseModel([])
        self.assertIsInstance(ba_kw12, BaseModel)
        self.assertIsInstance(ba_kw12.id, str)
        self.assertIsInstance(ba_kw12.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw12.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw12.__class__, type)

        ba_kw13 = BaseModel(())
        self.assertIsInstance(ba_kw13, BaseModel)
        self.assertIsInstance(ba_kw13.id, str)
        self.assertIsInstance(ba_kw13.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw13.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw13.__class__, type)

        ba_kw14 = BaseModel(1)
        self.assertIsInstance(ba_kw14, BaseModel)
        self.assertIsInstance(ba_kw14.id, str)
        self.assertIsInstance(ba_kw14.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw14.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw14.__class__, type)

        ba_kw15 = BaseModel("a")
        self.assertIsInstance(ba_kw15, BaseModel)
        self.assertIsInstance(ba_kw15.id, str)
        self.assertIsInstance(ba_kw15.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw15.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw15.__class__, type)

        ba_kw16 = BaseModel(None)
        self.assertIsInstance(ba_kw16, BaseModel)
        self.assertIsInstance(ba_kw16.id, str)
        self.assertIsInstance(ba_kw16.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw16.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw16.__class__, type)

        ba_kw17 = BaseModel({"first_name": "John"})
        self.assertIsInstance(ba_kw17, BaseModel)
        self.assertIsInstance(ba_kw17.id, str)
        self.assertIsInstance(ba_kw17.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw17.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw17.__class__, type)

        ba_kw18 = BaseModel(**{"my_list": [1, 2]})
        l14 = dir(ba_kw18)
        self.assertIn('my_list', l14)
        self.assertEqual(ba_kw18.__dict__['my_list'], [1, 2])
        # self.assertIsInstance(ba_kw18.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw18.updated_at, datetime.datetime)

        ba_kw19 = BaseModel(**{"my_tup": (1, 2)})
        l15 = dir(ba_kw19)
        self.assertIn('my_tup', l15)
        self.assertEqual(ba_kw19.__dict__['my_tup'], (1, 2))
        # self.assertIsInstance(ba_kw19.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw19.updated_at, datetime.datetime)

        ba_kw20 = BaseModel(**{"my_set": {1, 2}})
        l16 = dir(ba_kw20)
        self.assertIn('my_set', l16)
        self.assertEqual(ba_kw20.__dict__['my_set'], {1, 2})
        # self.assertIsInstance(ba_kw20.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw20.updated_at, datetime.datetime)

        ba_kw21 = BaseModel(**{"my_dict": {"a": 1}})
        l17 = dir(ba_kw21)
        self.assertIn('my_dict', l17)
        self.assertEqual(ba_kw21.__dict__['my_dict'], {"a": 1})
        # self.assertIsInstance(ba_kw20.created_at, datetime.datetime)
        # self.assertIsInstance(ba_kw20.updated_at, datetime.datetime)

    def test_save(self):
        """Test save method"""

        # storage = FileStorage()

        ba = BaseModel()
        temp = ba.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        ba.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(ba.__dict__['updated_at'], temp)
        temp = ba.__dict__['updated_at']
        # storage.reload()
        models.storage.reload()
        self.assertEqual(ba.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        ba = BaseModel()
        ba.age = 28
        ba.size = "tall"
        for k, v in ba.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, ba.to_dict())
                self.assertEqual(v, ba.to_dict()[k])
        self.assertEqual(ba.to_dict()['__class__'], ba.__class__.__name__)
        self.assertEqual(ba.to_dict()['updated_at'], ba.updated_at.isoformat())
        self.assertEqual(ba.to_dict()['created_at'], ba.created_at.isoformat())
        self.assertEqual(ba.to_dict()['age'], 28)
        self.assertEqual(ba.to_dict()['size'], 'tall')
        self.assertIsInstance(ba.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        ba = BaseModel()
        string = '['+ba.__class__.__name__+']'+' ('+ba.id+') '+str(ba.__dict__)
        self.assertEqual(string, ba.__str__())
