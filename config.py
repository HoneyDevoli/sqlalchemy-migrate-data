import os.path

# SQL configs
dbUser = ''
dbPassword = ''
dbName = 'test_db'
dbHost = 'localhost'
dbEngine = 'mysql+pymysql'

# Alchemy
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI ='{server}://{user}:{pw}@{url}/{db}'\
    .format(server=dbEngine, user=dbUser, pw=dbPassword, url=dbHost,
                                                            db=dbName)
