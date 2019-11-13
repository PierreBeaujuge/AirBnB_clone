#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines attributes/methods for the Review class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
