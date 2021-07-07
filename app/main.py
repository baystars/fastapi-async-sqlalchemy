# -*- mode: python -*- -*- coding: utf-8 -*-
from typing import List

import asyncio
from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import typer

from app.service.database import init_models
from app.models import City
from app.routers import router


app = FastAPI()
app.include_router(router)

cli = typer.Typer()


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


async def get_biggest_cities(session: AsyncSession) -> List[City]:
    result = await session.execute(select(City).order_by(City.population.desc()).limit(20))
    return result.scalars().all()


def add_city(session: AsyncSession, name: str, population: int):
    new_city = City(name=name, population=population)
    session.add(new_city)
    return new_city

    
if __name__ == "__main__":
    cli()
