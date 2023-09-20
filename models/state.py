#!/usr/bin/python3
"""State Module for HBNB project."""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models import storage
import os


class State(BaseModel, Base):
    """State class ."""

    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """Getter."""
        listCities = []
        for city in storage.all("City"):
            if city.state_id == self.id:
                listCities.append(city)
        return listCities
