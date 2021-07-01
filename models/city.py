#!/usr/bin/python3
""" city module """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
