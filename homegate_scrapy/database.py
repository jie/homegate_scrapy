#!/usr/bin/env python
# encoding: utf-8
# @author: ZhouYang

from pony.orm import *
from settings import DATABASE

db = Database(
    "mysql",
    **DATABASE
)


class Hacknews(db.Entity):
    identity = PrimaryKey(int)
    title = Required(str, 128)
    link = Required(str, 128)


sql_debug(False)
db.generate_mapping()
