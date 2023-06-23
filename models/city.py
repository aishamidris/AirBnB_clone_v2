#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import column, foreignkey, string

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = columin(string(60), foreignkey(states.id),  nullable=False
    name = columin(string(128), nullable=False
