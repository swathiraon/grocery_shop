from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Grocery(Base):
	__tablename__ = 'grocery'
	id = Column(Integer,primary_key = True)
	product = Column(String(200),nullable = False)
	price = Column(Integer)
	quantity = Column(String)




engine = create_engine("sqlite:///grocery.db")
Base.metadata.create_all(engine)























