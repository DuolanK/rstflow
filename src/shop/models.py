from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey

metadata = MetaData()

shop = Table(
    "shop",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("creator_id", Integer),
)

