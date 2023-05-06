
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("name", String),
    Column("date", type_=TIMESTAMP(timezone=True)),
    Column("description", String),
)