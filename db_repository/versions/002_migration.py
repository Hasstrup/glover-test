from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event_component = Table('event_component', pre_meta,
    Column('event_id', INTEGER, primary_key=True, nullable=False),
    Column('component_id', INTEGER, primary_key=True, nullable=False),
)

event_vendor = Table('event_vendor', post_meta,
    Column('event_id', Integer, primary_key=True, nullable=False),
    Column('vendor_id', Integer, primary_key=True, nullable=False),
)

Component = Table('Component', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=120)),
    Column('Max_price', Integer),
    Column('Min_price', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event_component'].drop()
    post_meta.tables['event_vendor'].create()
    post_meta.tables['Component'].columns['Max_price'].create()
    post_meta.tables['Component'].columns['Min_price'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event_component'].create()
    post_meta.tables['event_vendor'].drop()
    post_meta.tables['Component'].columns['Max_price'].drop()
    post_meta.tables['Component'].columns['Min_price'].drop()
