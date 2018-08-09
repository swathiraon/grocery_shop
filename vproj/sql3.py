from sql2 import *
from tabulate import tabulate
while True:
	print("what you like to do?")
	option=[(1,"add products"),
		(2,"delete products"),
		(3,"display products"),
		(4,"modify by id"),
		(5,"view by id"),
		(6,"view_name"),
		(7,"modify_by_name"),
		(8,"quit")
		]
	print(tabulate(option,tablefmt="fancy_grid"))
	ch=input()
	if ch=="1":
		add_products()
	elif ch=="2":
		del_products()

	else:
		display()

	elif ch=="3":
		display()
	elif ch=="4":
		modify_id()
	elif ch=="5":
		view_id()
	elif ch=="6":
		view_name()
	elif ch=="7":
		modify_by_name()
	elif ch=="8":
		print("thank you")
		quit()



		


			