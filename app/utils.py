# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import HTTPException


class DuplicatedEntryError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=422, detail=message)