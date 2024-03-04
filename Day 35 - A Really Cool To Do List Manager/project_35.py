import os, time
toDoList=[]

def printList():
  print()
  if len(toDoList) == 0:
    print("Your list is empty 🥳")
  else:
    print("Your 'To Do' list:")
    for item in toDoList:
      print(item)

while True:
  action = input("To Do List Manager\nDo you want to view, add, edit, or remove an item from the 'To Do' list?\n")
  if action == "view":
    printList()
  elif action == "add":
    print()
    item = input("What do you want to add?\n").title()
    toDoList.append(item)
  elif action == "remove":
    print()
    item = input("What do you want to remove?\n").title()
    if item in toDoList:
      answer = input("Are you sure you want to remove this?\n")
      if answer == "yes":
        toDoList.remove(item)
      else:
        continue
    else:
      print(f"{item} is not on the list")
  elif action == "edit":
    print()
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(toDoList)):
      if toDoList[i]==item:
        toDoList[i]=new
  else:
    answer = input("Invalid input. Do you want to exit? (yes/no)\n")
    if answer == "yes":
      break
    else:
      continue
  time.sleep(2)
  os.system('clear')