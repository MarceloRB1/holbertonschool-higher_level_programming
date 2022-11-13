#!/usr/bin/python3
'''
Model state from task 6
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''
    Define a class called state
    that inherits from Base
    This class represent a SQL table
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True
                )
    name = Column(String(128), nullable=False)
