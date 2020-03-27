# pip install psycopg2==2.6.1 Flask-SQLAlchemy===2.1 Flask-Migrate==1.8.0

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
db = declarative_base(engine)

import db_setting.models



