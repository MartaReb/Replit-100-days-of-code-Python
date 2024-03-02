print("To Do List Manager")
print()

toDoList=[]
def printList():
  if len(toDoList) == 0:
    print()
    print("Your list is empty 🥳")
  else:
    print()
    print("Your 'To Do' list:")
    for item in toDoList:
      print(item)

while True:
  print()
  action = input("Do you want to view, add, or edit your 'To Do' list?\n")
  if action == "view":
    printList()
  elif action == "add":
    print()
    item = input("What do you want to add?\n")
    toDoList.append(item)
    printList()
  elif action == "edit":
    print()
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
  else:
    answer = input("Invalid input. Do you want to exit? (yes/no)\n")
    if answer == "yes":
      break
    else:
      continue