#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines attributes/methods for the City class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    state_id = ""
    name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
