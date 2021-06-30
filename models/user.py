#!/usr/bin/python3
""" define user module """

from models.base_model import BaseModel


class User(BaseModel):
    """ user class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
