#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Enum,ForeignKey,UniqueConstraint,ForeignKeyConstraint,Index
from sqlalchemy.orm import sessionmaker, relationship

egine=create_engine('mysql+pymysql://root@127.0.0.1:3306/db1?charset=utf8',max_overflow=5)

Base=declarative_base()

#创建单表:业务线
class Business(Base):
    __tablename__='business'
    id=Column(Integer,primary_key=True,autoincrement=True)
    bname=Column(String(32),nullable=False,index=True)

class Service(Base):
    business_id = Column(Integer, )


