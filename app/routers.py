# -*- mode: python -*- -*- coding: utf-8 -*-
from typing import List

from fastapi import (Depends, APIRouter)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import City
from app.utils import DuplicatedEntryError
from app.service.database import get_session
from app.service.database import query


router = APIRouter()


@router.get("/cities/", response_model=List[City])
async def get_biggest_cities(session: AsyncSession=Depends(get_session)):
    cities = await query.get_biggest_cities(session)
    return [City(name=c.name, population=c.population) for c in cities]


@router.post("/cities/")
async def add_city(city: City, session: AsyncSession=Depends(get_session)):
    city = query.add_city(session, city.name, city.population)
    try:
        await session.commit()
        return city
    except IntegrityError as ex:
        await session.rollback()
        raise DuplicatedEntryError("The city is already stored")