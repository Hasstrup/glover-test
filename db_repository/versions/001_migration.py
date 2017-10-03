from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=12)),
    Column('email', VARCHAR),
)

Component = Table('Component', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=120)),
)

Event = Table('Event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('user_id', Integer),
)

User = Table('User', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=12)),
    Column('email', String),
)

Vendor = Table('Vendor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('vendorname', String(length=120)),
    Column('email', String(length=120)),
    Column('component_id', Integer),
)

event_component = Table('event_component', post_meta,
    Column('event_id', Integer, primary_key=True, nullable=False),
    Column('component_id', Integer, primary_key=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    post_meta.tables['Component'].create()
    post_meta.tables['Event'].create()
    post_meta.tables['User'].create()
    post_meta.tables['Vendor'].create()
    post_meta.tables['event_component'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    post_meta.tables['Component'].drop()
    post_meta.tables['Event'].drop()
    post_meta.tables['User'].drop()
    post_meta.tables['Vendor'].drop()
    post_meta.tables['event_component'].drop()
