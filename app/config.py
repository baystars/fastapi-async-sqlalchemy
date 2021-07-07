# -*- mode: python -*- -*- coding: utf-8 -*-
import os
from pathlib import Path


APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = Path(APP_DIR).parent
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATABASE_URL = f'sqlite+aiosqlite:///{DATA_DIR}/data.db'