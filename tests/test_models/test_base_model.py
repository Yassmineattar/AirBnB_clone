#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
import models
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test methods."""
        self.instance = BaseModel()

    def tearDown(self):
        """Clean up after test methods."""
        del self.instance

    def test_instance_creation(self):
        """Test that a new instance is correctly created."""
        self.assertIsInstance(self.instance, BaseModel)
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique id."""
        another_instance = BaseModel()
        self.assertNotEqual(self.instance.id, another_instance.id)
        del another_instance

    def test_str_method(self):
        """Test the __str__ method."""
        string_representation = self.instance.__str__()
        expected = f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_representation, expected)

    def test_save_method(self):
        """Test the save method."""
        old_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(old_updated_at, self.instance.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        instance_dict = self.instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], self.instance.id)
        self.assertEqual(instance_dict['created_at'], self.instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'], self.instance.updated_at.isoformat())
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        data = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'Test'
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, data['id'])
        self.assertEqual(instance.created_at.isoformat(), data['created_at'])
        self.assertEqual(instance.updated_at.isoformat(), data['updated_at'])
        self.assertEqual(instance.name, 'Test')
        del instance


if __name__ == '__main__':
    unittest.main()
