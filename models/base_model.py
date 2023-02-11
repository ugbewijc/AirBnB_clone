#!/usr/bin/python3
"""Defines BaseModel Class"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """"initialize class"""
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(
                    self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                    self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary of  all keys/values of __dict__"""
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()
        return mydict
