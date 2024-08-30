from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base #sqlarchemy: orm

Base = declarative_base()

# 테이블 구조 선언하기
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    created_at = Column(DateTime)
