from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, DateTime, JSON

metadata = MetaData()

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", Integer),
    Column("shop_id", Integer),
    Column("client_id", Integer),
    Column("created_at", type_=TIMESTAMP(timezone=True)),
    Column("done_until", type_=TIMESTAMP(timezone=True)),
    Column("status", JSON),
)