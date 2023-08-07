from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey, Boolean

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("shop_id", Integer),
    Column("quantity", Integer),
    Column("price", Integer),
    Column("name", String),
    Column("prep_time", Integer),
    Column("description", String),
    Column("is_available", Boolean),
)

