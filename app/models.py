# -*- mode: python -*- -*- coding: utf-8 -*-
from sqlalchemy import (Column, String, Integer)

from app.service.database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    population = Column(Integer)
