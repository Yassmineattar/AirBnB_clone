#!/usr/bin/python3
"""
    This if __init__ file to create a unique FileStorage instance
"""
import os
from models.engine.db_storage import DBStorage
from models.engine import file_storage

if os.getenv('HBNB_TYPE_STORAGE') == "db":

    storage = DBStorage()
else:

    storage = FileStorage()
storage.reload()
