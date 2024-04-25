import time, os
inventory = []

try:
  file = open("inventory.txt", "r")
  inventory = eval(file.read())
  file.close()
except:
  pass

def add():
  print()
  add_item= input("Input the item to add:\n> ").title()
  inventory.append(add_item)
  print(f"{add_item} has been added to your inventory.")

def remove():
  print()
  remove_item = input("Input the item to remove:\n> ").title()
  if remove_item in inventory:
    inventory.remove(remove_item)
    print(f"{remove_item} has been removed from your inventory.")
  else:
    print("You don't have that item.")

def view():
  print()
  print("Inventory")
  print("=========")
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)
                 
while True:
  print("RPG Inventory")
  print()
  menu = input("1: Add  2: Remove  3: View\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    remove()
  elif menu == "3":
    view()
  else:
    print("Invalid input")
  time.sleep(3)
  os.system("clear")
  
  file = open("inventory.txt", "w")
  file.write(str(inventory))
  file.close()