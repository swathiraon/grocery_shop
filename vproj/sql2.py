from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,update
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
	set_status(addp)
	session.add(addp)
	session.commit()




def del_products():

	disp_id()
	i=int(input("Enter the id"))
	session.query(Grocery).filter_by(id=i).delete()
	session.commit()







def display():

	list=[]
	items=session.query(Grocery).all()
	
	list.append(("Id ","Product","Price","Quantity","Status"))
	
	for l in items:
		list.append((l.id,l.product,l.price,l.quantity,l.status))

	print(tabulate(list,tablefmt="fancy_grid"))




def update_quantity():

	q=int(input("1.Increment \n 2.Decrement\n"))
	disp_id()
	


	if q==1:
		i=int(input("Enter ID"))
		r=int(input("Enter the number by which the quantity has to be incremented "))
		session.query(Grocery).\
	 	filter(Grocery.id==i).\
	 	update({"quantity":(Grocery.quantity+r)})
		session.commit()
		if(session.query(Grocery).filter(Grocery.id==i).one().quantity<=0):
			update_status(1,i)
		elif(session.query(Grocery).filter(Grocery.id==i).one().quantity>0):
			update_status(2,i)
		else:print(" ")
		
	elif q==2:
		i=int(input("Enter ID"))
		s=i
		r=int(input("Enter the number by which the quantity has to be decremented "))
		session.query(Grocery).\
			filter( Grocery.id== i).\
			update({"quantity": (Grocery.quantity -r)})
		session.commit()
		if(session.query(Grocery).filter(Grocery.id==i).one().quantity<=0):
			update_status(1,i)
			
	else:
		print("Invalid input")





def update_status(x,i):

	if x==1:
		session.query(Grocery).\
			filter( Grocery.id== i).\
			update({"status": "Out of stock"})
		session.commit()
		session.query(Grocery).\
			filter( Grocery.id== i).\
			update({"quantity": (Grocery.quantity-Grocery.quantity)})
		
		session.commit()

	elif x==2:
		session.query(Grocery).\
			filter( Grocery.id== i).\
			update({"status": "In stock"})
		session.commit()




def set_status(addp):

	if(addp.quantity<=0):
		addp.status="Out of Stock"

	else:
		addp.status="In Stock"



def disp_id():

	list=[]
	items=session.query(Grocery).all()
	
	list.append(("Id ","Product"))
	
	for l in items:
		list.append((l.id,l.product))

	print(tabulate(list,tablefmt="fancy_grid"))



def check_status():

	disp_id()
	i=int(input("\nEnter Id\n"))
	print(session.query(Grocery).filter(Grocery.id==i).one().status)



