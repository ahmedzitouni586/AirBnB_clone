#!/usr/bin/python3
""" base model module """

import uuid
import datetime
from models.__init__ import storage
import models
form = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        """instantiation of attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.datetime.strptime(
            kwargs["created_at"], form)
            self.updated_at = datetime.datetime.strptime(
            kwargs["updated_at"], form)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
            models.storage.save

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__> """
        return("[{}] ({}) {}".format
        (self.__class__.__name__, self.id,
        self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at 
        with the current datetime
        """
        updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance:
        """
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['updated_at'] = self.updated_at.isoformat()
        d['created_at'] = self.created_at.isoformat()
        return d
