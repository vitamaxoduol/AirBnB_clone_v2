#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from  os import environ


metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                        Column("place_id", String(60), ForeignKey("places.id"), primary_key = True, nullable = False),
                        Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key = True, nullable = False)
                        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable = False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable = False)
    name = Column(String(128), nullable = False)

    description = Column(String(1024))
    number_rooms = Column(Integer, nullable = False, default = 0)
    number_bathrooms = Column(Integer, nullable = False, default = 0)
    max_guest = Column(Integer, nullable = False, default = 0)

    price_by_night = Column(Integer, nullable = False, default = 0)
    latitude = Column(Integer, nullable = False, default = 0)
    longitude = Column(Integer, nullable = False, default = 0)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref = "place", cascade = "all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity", backref = "place_amenities", viewonly = False)
        
    @property
    def reviews(self):
        """Find the reviews associated to a place_id"""
        from models import storage
        if environ.get("HBNB_TYPE_STORAGE") == "db":
            return
        objs = []
        all_objs = storage.all(Review)
        for item in all_objs.values():
            if item.place_id == self.id:
                objs.append(item)
        return objs
