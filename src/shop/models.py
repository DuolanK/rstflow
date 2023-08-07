from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey, DateTime, Boolean, Float

metadata = MetaData()

shop = Table(
    "shop",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("creator_id", Integer),
    Column("is_active", Boolean),
    Column("work_time_from", DateTime.Time),
    Column("work_time_to", DateTime.Time),
    Column("latitude", Float),
    Column("longitude", Float),
)

