#!/usr/bin/python3

"""defines Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
