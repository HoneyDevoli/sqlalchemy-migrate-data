from migrate import DatabaseAlreadyControlledError
from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
import os.path
from db_setting import db, engine
from sqlalchemy_utils import database_exists, create_database


def create_db(db_engine):
    if database_exists(db_engine.url):
        print('Database already exists')
    else:
        create_database(db_engine.url)
        db.metadata.create_all()
        print('Database was created')


def create_migrate_dir(db_engine, path_to_migrate_dir):
    if not os.path.exists(path_to_migrate_dir):
        api.create(path_to_migrate_dir, 'database repository')
        api.version_control(db_engine, path_to_migrate_dir)
        print('Migration dir created: ' + path_to_migrate_dir)
    else:
        # create system table for sqlalchemy migration
        try:
            api.version_control(db_engine, path_to_migrate_dir, api.version(path_to_migrate_dir))
        except DatabaseAlreadyControlledError:
            print('<migrate_version> table already exists')


create_db(engine)
create_migrate_dir(engine, SQLALCHEMY_MIGRATE_REPO)

from db_setting import Session
from db_setting.models import Man

session = Session()
session.query()
man = Man("Ivan Ivanovish Ivanov")
session.add(man)
session.commit()
session.close()