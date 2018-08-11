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
	if quantity > 0:
		addp = Grocery(product = product,price = price,quantity = quantity,status="in stock")
	else:
		addp = Grocery(product = product,price = price,quantity = quantity,status="out stock")
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

	a = session.query(Grocery).all()	
	list.append(("Id ","Product","Price","Quantity","status"))
	for l in a:
		list.append((l.id,l.product,l.price,l.quantity,l.status))
	print(tabulate(list,tablefmt="fancy_grid"))



def modify_id():
	v=[]
	display()
	id=input("enter the item id")
	a = session.query(Grocery).filter(Grocery.id==id).one()
	print("what do you want to modify")
	option=[(1,"price"),
		(2,"quantity")]
	print(tabulate(option,tablefmt="fancy_grid"))
	choice=input("enter your choice")
	if choice=="1":
		price=input("enter the new price")
		a.price=price

		session.commit()

	elif choice=="2":
		quantity=input("enter the new quantity in with the + or - infront of it")
		sign=quantity[0]
		number=quantity[1:]

		if sign =="+":

			a.quantity=a.quantity+number
			a.status="in stock"
			session.commit()
		elif sign == "-":
		
			if a.quantity-number<0:
				print("only ",a.quantity ,"amount of ", a.product ,"is left")

			else:
				if a.quantity-number == 0:

					a.quantity=a.quantity-number
					a.status='out stock'
					session.commit()
				else :
					a.quantity=a.quantity-number
					a.status='in stock'
					session.commit()
	
	print("modified")

def view_id():
	id=input("enter the id")
	a = session.query(Grocery).filter(Grocery.id==id).one()
	list=[]
	list.append(("Id ","Product","Price","Quantity","status"))
	list.append((a.id,a.product,a.price,a.quantity,a.status))
	print(tabulate(list,tablefmt="fancy_grid"))

def view_name():
	name=input("enter the name of the product")
	a = session.query(Grocery).filter(Grocery.product==name).one()
	list=[]
	list.append(("Id ","Product","Price","Quantity","status"))
	list.append((a.id,a.product,a.price,a.quantity,a.status))
	print(tabulate(list,tablefmt="fancy_grid"))

def modify_by_name():
	new=input("enter the name and the quantity to be modified with + or - in front of the quantity")
	k=new.split(" ")
	name=k[0]
	sign=k[1][0]
	number=int(k[1][1:])
	a = session.query(Grocery).filter(Grocery.product==name).one()
	if sign =="+":
		
		a.quantity=a.quantity+number
		session.commit()

	elif sign == "-":
		
		if a.quantity-number<0:
			print("only ",a.quantity ,"amount of ", name ,"is left")

		else:
			if a.quantity-number == 0:

				a.quantity=a.quantity-number
				a.status='out stock'
				session.commit()
			else :
				a.quantity=a.quantity-number
				a.status='in stock'
				session.commit()
	print("modified")





