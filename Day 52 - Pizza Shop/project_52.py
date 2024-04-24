import os, time
pizzas=[]

try:
  f = open("pizza.txt", "r")
  pizzas = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza list, using a blank list")

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Your name please: ").title()
  size = input("Choose the size (s/m/l): ")
  while True:
    try:
      qty = int(input("How many pizzas? "))
      break
    except:
      print("You must input a numerical character! Please, try again.")
      pass
  cost= 0
  if size =="s":
    cost = 4.99
  elif size =="m":
    cost = 7.99
  else:
    cost = 12.99
  total = cost * qty
  total = round(total, 2)
  row = [name, size, qty, total]
  pizzas.append(row)

def view():
  for row in pizzas:
    print(f"Name: {row [0]},\nSize: {row [1]},\nQuantity: {row [2]},\nTotal: {row [3]} dollars.\n")
  time.sleep(3)
  
while True:
  time.sleep(1)
  os.system("clear")
  print("The Best Pizza")
  print()
  menu = input("Choose:\n1.Add order\n2.View orders\n> ")
  if menu =="1":
    add()
  elif menu =="2":
    view()
  else:
    print("Please, choose a valid option!")
  f = open("pizza.txt", "w")
  f.write(str(pizzas))
  f.close()