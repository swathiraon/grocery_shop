from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sql1 import Grocery,Base

engine  = create_engine("sqlite:///grocery.db")

Base.metadata.bind = engine

Session  = sessionmaker(bind = engine)

session = Session()


def add_products():
	product = input("enter product name")
	price = int(input("enter the price"))
	quantity = int(input("enter the quantity"))
	addp = Grocery(product = product,price = price,quantity = quantity)
	session.add(addp)
	session.commit()

def del_products():
	product = input("enter product name")
	price = int(input("enter the price"))
	quantity = int(input("enter the quantity"))
	delp = Grocery(product = product,price = price,quantity = quantity)
	session.delete(delp)
	session.commit()

def display():
	a = session.query(Grocery).all()	
	return a