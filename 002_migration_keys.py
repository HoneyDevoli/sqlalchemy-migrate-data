from sqlalchemy import *
from migrate import *

from migrate.changeset import schema

pre_meta = MetaData()
post_meta = MetaData()

man = Table('man', pre_meta,
            Column('full_name', VARCHAR(length=1024), primary_key=True, nullable=False),
            )

work_place = Table('work_place', pre_meta,
                   Column('id', INTEGER, primary_key=True, nullable=False),
                   Column('place_name', VARCHAR(length=1024), nullable=False),
                   Column('full_name', VARCHAR(length=1024))
                   )
man_workplace_fk = ForeignKeyConstraint(columns=[work_place.c.full_name], refcolumns=[man.c.full_name], name='man_workplace_fk')


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine

    # _t = Table('work_place', pre_meta, autoload=True) # autoload table from db

    man_workplace_fk.drop()
    pre_meta.tables['man'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine

    pre_meta.tables['man'].create()
    man_workplace_fk.create()
