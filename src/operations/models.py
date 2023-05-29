from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", Integer),
    Column("price", Integer),
    Column("creator_id", Integer),
    Column("name", String),
    Column("date", type_=TIMESTAMP(timezone=True)),
    Column("time", Integer),
    Column("description", String),
)