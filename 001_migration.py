from sqlalchemy import *
from migrate import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker

pre_meta = MetaData()
post_meta = MetaData()

pre_man = Table('man', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('full_name', VARCHAR(length=4096), nullable=False),
)
class PreMan(object):
    def __init__(self, full_name):
        self.full_name = full_name


post_man = Table('man', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=4096), nullable=False),
    Column('second_name', String(length=4096), nullable=False),
    Column('last_name', String(length=4096), nullable=False),
)
class PostMan(object):
    def __init__(self, f_name, s_name, l_name):
        self.first_name = f_name
        self.second_name = s_name
        self.last_name = l_name

mapper(PreMan, pre_man)
mapper(PostMan, post_man)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine

    Session = sessionmaker(bind=migrate_engine)
    session = Session()
    pre_man_record = session.query(PreMan).filter(PreMan.full_name.contains('Ivan')).one()
    session.close()

    pre_meta.tables['man'].columns['full_name'].drop()
    post_meta.tables['man'].columns['first_name'].create()
    post_meta.tables['man'].columns['last_name'].create()
    post_meta.tables['man'].columns['second_name'].create()

    f_name, s_name, l_name = pre_man_record.full_name.split(' ')
    post_man_record = PostMan(f_name, s_name, l_name)
    session = Session()
    session.add(post_man_record)
    session.commit()
    session.close()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    Session = sessionmaker(bind=migrate_engine)

    session = Session()
    post_man_record = session.query(PostMan).filter(PostMan.first_name == 'Ivan').one()
    session.close()

    pre_meta.tables['man'].columns['full_name'].create()
    post_meta.tables['man'].columns['first_name'].drop()
    post_meta.tables['man'].columns['last_name'].drop()
    post_meta.tables['man'].columns['second_name'].drop()

    session = Session()
    pre_man_record = PreMan("{0} {1} {2}".format(post_man_record.first_name, post_man_record.second_name, post_man_record.last_name))
    session.add(pre_man_record)
    session.commit()
    session.close()

