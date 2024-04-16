pizzas=[]

def add():
  name = input("Your name please: ").title()
  size = input("Choose the size (s/m/l): ")
  while True:
    try:
      num_pizzas = int(input("How many pizzas? "))
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
  total = cost * num_pizzas
  total = round(total,2)
  pizzas.append(name)
  pizzas.append(size)
  pizzas.append(num_pizzas)
  pizzas.append(total)

add()
print()
print(f"Thanks {pizzas[0]}, your pizza(s) will cost {pizzas[3]} dollars.")