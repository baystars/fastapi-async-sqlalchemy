from typing import List

import asyncio
import typer
from fastapi import (FastAPI, Depends)

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils import DuplicatedEntryError
from app.service.database import (init_models, get_session)
from app import (models, schemas)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()
cli = typer.Typer()

@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


@app.get("/cities/biggest", response_model=List[schemas.City])
async def get_biggest_cities(session: AsyncSession=Depends(get_session)):
    cities = await get_biggest_cities(session)
    return [schemas.City(name=c.name, population=c.population) for c in cities]


@app.post("/cities/")
async def add_city(city: schemas.City, session: AsyncSession=Depends(get_session)):
    city = add_city(session, city.name, city.population)
    try:
        await session.commit()
        return city
    except IntegrityError as ex:
        await session.rollback()
        raise DuplicatedEntryError("The city is already stored")


async def get_biggest_cities(session: AsyncSession) -> List[models.City]:
    result = await session.execute(select(models.City).order_by(models.City.population.desc()).limit(20))
    return result.scalars().all()


def add_city(session: AsyncSession, name: str, population: int):
    new_city = models.City(name=name, population=population)
    session.add(new_city)
    return new_city
    
if __name__ == "__main__":
    cli()
