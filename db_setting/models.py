from sqlalchemy.orm import relationship

from db_setting import db
from sqlalchemy import Column, Integer, String, ForeignKey


class Man(db):
    __tablename__ = 'man'

    full_name = Column('full_name', String(1024), nullable=False, primary_key=True)
    work_place = relationship('WorkPlace', uselist=False, back_populates='man')

    def __init__(self, full_name):
        self.full_name = full_name

class WorkPlace(db):
    __tablename__ = 'work_place'

    id = Column(Integer, primary_key=True, autoincrement=True)
    place_name = Column(String(length=1024), nullable=False)
    full_name = Column(String(length=1024), ForeignKey('man.full_name', name='man_workplace_fk'))

    man = relationship('Man', uselist=False, back_populates='work_place')

    def __init__(self, full_name, place_name):
        self.full_name = full_name
        self.place_name = place_name

# new model

# class Man(db):
#     __tablename__ = 'man'
#
#     first_name = Column(String(length=1024), nullable=False)
#     second_name = Column(String(length=1024), nullable=False)
#     last_name = Column(String(length=1024), nullable=False, primary_key=True)
#     work_place = relationship('WorkPlace', uselist=False, back_populates='man')
#
#     def __init__(self, f_name, s_name, l_name):
#         self.first_name = f_name
#         self.second_name = s_name
#         self.last_name = l_name
#
# class WorkPlace(db):
#     __tablename__ = 'work_place'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     place_name = Column(String(length=1024), nullable=False)
#     full_name = Column(String(length=1024), ForeignKey('man.full_name'))
#
#     man = relationship('Man', uselist=False, back_populates='work_place')
#
#     def __init__(self, full_name, place_name):
#         self.full_name = full_name
#         self.place_name = place_name


