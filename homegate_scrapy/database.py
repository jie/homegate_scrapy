#!/usr/bin/env python
# encoding: utf-8
# @author: ZhouYang

from datetime import datetime
from pony.orm import *
from settings import DATABASE

db = Database(
    "mysql",
    **DATABASE
)


class News(db.Entity):
    identity = Required(str, 36)
    title = Required(str, 128)
    link = Required(str, 256)
    description = Optional(str, 256)
    content = Optional(str, nullable=True)
    author = Optional(str, nullable=True)
    site = Required(str, 36, nullable=True)
    tag = Optional(str, 64, nullable=True)
    category = Optional(str, 32, nullable=True)
    showcase = Optional(str, 32, nullable=True)
    create_at = Optional(datetime, nullable=True)


sql_debug(False)
db.generate_mapping()
