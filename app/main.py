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
def db_init_models(drop: bool = typer.Argument(False)):
    asyncio.run(init_models(drop))
    print("Done")

    
if __name__ == "__main__":
    cli()
