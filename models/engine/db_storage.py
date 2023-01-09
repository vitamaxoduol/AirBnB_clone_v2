#!/usr/bin/python3
"""Create a database storage"""
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.base_model import BaseModel, Base


class DBStorage:
    """Class DBStorage to define interactions with a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Create and initialize attributes"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".format(environ.get("HBNB_MYSQL_USER"),\
                                    environ.get("HBNB_MYSQL_PWD"), environ.get("HBNB_MYSQL_HOST"),\
                                    environ.get("HBNB_MYSQL_DB")), pool_pre_ping = True\
                                    )
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Querry the database session for all objects of the same type"""
        objs = {}
        if (cls):
            res = self.__session.query(cls).all()
        else:
            res = self.__session.query(State).join(City).join(User).all()
        for item in res:
            objs[f"{item.__class__}.{item.id}"] = str(item)
        return objs

    def new(self, obj):
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Save the state of the current session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete a passed object from the database"""
        if obj:
            session.delete(obj)
            session.commit()

    def reload(self):
        """create all tables from the database"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit = False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
