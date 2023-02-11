#!/usr/bin/python3

"""Defines User Class"""

from models.base_model import BaseModel


class User (BaseModel):
    """User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
