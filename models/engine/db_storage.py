#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone."""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Definition of class dbStorage."""

    __engine = None
    __session = None

    def __init__(self):
        """Instatntiate a dbStorage."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrive Data fro DB."""
        results = {}
        if cls is not None:
            for item in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, item.id)
                results[key] = item
        else:
            for c_name, item in Base.metadata.tables.items():
                cls = c_name
                for item in self.__session.query(cls).all():
                    key = "{}.{}".format(cls.__name__, item.id)
                    results[key] = item
        return results

    def new(self, obj):
        """Add new Item to the DB."""
        self.__session.add(obj)

    def save(self):
        """Commit changes to DB."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delte Item from DB."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in DB."""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()
