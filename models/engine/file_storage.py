#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances.
      Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects
      Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self):deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_obj = {}
        for key, obj in self.__objects.items():
            dict_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(dict_obj, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State, 'Place': Place, 'City': City,
            'Amenity': Amenity, 'Review': Review
        }
        if os.path.exists(self.__file_path) and\
                os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)  # Read the file content as a string
                for key, obj_data in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name in classes:
                        self.__objects[key] = classes[class_name](**obj_data)
