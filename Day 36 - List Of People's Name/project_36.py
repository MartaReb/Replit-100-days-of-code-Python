listName = []

def printListName():
  print()
  for name in listName:
    print(name)
  print()
  
while True:
  first = input("First name: ").strip().capitalize()
  last = input("Last name: ").strip().capitalize()
  name = f"{first} {last}"
  if name not in listName:
    listName.append(name)
  else:
    print("Those names are already in the list.")
  printListName()