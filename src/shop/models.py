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
    Column("work_time_from", TIMESTAMP(timezone=False), nullable=False, default='08:00'),
    Column("work_time_to", TIMESTAMP(timezone=False), nullable=False, default='08:00'),
    Column("latitude", Float),
    Column("longitude", Float),
)

Column('timestamp', )