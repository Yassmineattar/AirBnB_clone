#!/usr/bin/python3
"""This class named BaseModel that defines all common attributes/methods
    for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Public Attributes:
            id : UUID4 generated ad converted to string
            created_at : datetime assign when instance created
            updated_at : datetime assign when instance updated

        Public Methods:
            save(self): updates the instance attribute
                        updated_at with current datetime
            to_dict(self): returns a dictionary with all keys/values
    """

    def __init__(self, *args, **kwargs):
        """constructor of the BaseModel class
        Initialization method for att attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
