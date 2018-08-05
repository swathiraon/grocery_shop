from sql2 import *
while True:
	print("what you like to do?")
	ch = input(" 1.Add products\n 2.Delete products\n 3.display\n 4.update quantity\n 5.check status \n 6.exit")
	if ch=="1":
		add_products()
	elif ch=="2":
		del_products()
	elif ch=="3": 
		display()

	elif ch=="4":
		update_quantity()

	elif ch=="5":
		check_status()

	else:
		exit()
		


			