#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class Amenity(BaseModel, Base):
    """Create an aneminities"""
    __tablename__ = "amenity"
    name = Column(String(60), nullable = False)
