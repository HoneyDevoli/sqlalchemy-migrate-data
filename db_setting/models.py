from db_setting import db
from sqlalchemy import Column, Integer, String


class Man(db):
    __tablename__ = 'man'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column('full_name', String(4096), nullable=False)

    def __init__(self, full_name):
        self.full_name = full_name



# new model

# class Man(db):
#     __tablename__ = 'man'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     first_name = Column(String(length=4096), nullable=False)
#     second_name = Column(String(length=4096), nullable=False)
#     last_name = Column(String(length=4096), nullable=False)
#
#     def __init__(self, f_name, s_name, l_name):
#         self.first_name = f_name
#         self.second_name = s_name
#         self.last_name = l_name

