from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sql1 import Grocery,Base
from tabulate import tabulate

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

	list=[]
	items=session.query(Grocery).all()
	
	list.append(("Id ","Product"))
	#print(tabulate(v,tablefmt="fancy_grid"))
	for l in items:
		list.append((l.id,l.product))

	print(tabulate(list,tablefmt="fancy_grid"))

		



	
	i=int(input("Enter the id"))
	session.query(Grocery).filter_by(id=i).delete()
	session.commit()


def display():
	list=[]
	items=session.query(Grocery).all()
	
	list.append(("Id ","Product","Price","Quantity"))
	#print(tabulate(v,tablefmt="fancy_grid"))
	for l in items:
		list.append((l.id,l.product,l.price,l.quantity))

	print(tabulate(list,tablefmt="fancy_grid"))
