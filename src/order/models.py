
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", Integer),
    Column("creator_id", Integer),
    Column("date", type_=TIMESTAMP(timezone=True)),
)