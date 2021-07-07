# -*- mode: python -*- -*- coding: utf-8 -*-
from pydantic import BaseModel

class City(BaseModel):
    name: str
    population: int
