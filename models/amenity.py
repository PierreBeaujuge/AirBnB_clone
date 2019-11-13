#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
Amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines attributes/methods for the Amenity class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
