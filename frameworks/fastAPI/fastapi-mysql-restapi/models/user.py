from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

users = Table(
  "user",
  meta,
  Column("id", Integer, primary_key=True),
  Column("name", String(255)),
  Column("email", String(255)),
  Column("password", String(255)),
)

meta.create_all(engine)