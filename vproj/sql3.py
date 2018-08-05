from sql2 import *
while True:
	print("what you like to do?")
	ch = input("1.Add products\n2.Delete products\n3.display")
	if ch=="1":
		add_products()
	elif ch=="2":
		del_products()
	else:
		list = display()
		tab = []
		for i in list:
			tab.append(i.product)
			tab.append(i.price)
			tab.append(i.quantity)
		print(tab)


			