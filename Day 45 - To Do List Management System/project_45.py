import os
print("🌟 Life Organizer 🌟")
print()
print("Welcome to the life organizer.")
list = []

def add():
  task = input("What is the task? > ").strip().title()
  due = input("When is it due by? > ").strip()
  priority = input("What is the priority (high, medium or low)? > ").strip().title()
  list.append([task, due, priority])
  print()
  print("Thanks, this task has been added.")
  
def view():
  for row in list:
    print(row)

def edit():
  task = input("Which task do you want to edit? > ").strip().title()
  for row in list:
    if task in row:
      list.remove(row)
      new_task = input("What is the new task? > ").strip().lower() 
      new_due = input("What is the new due date? > ").strip()
      new_priority = input("What is the new priority? > ").strip().lower()
      list.append([new_task, new_due, new_priority])

def remove():
  task = input("Which task do you want to remove? > ").strip().title()
  for row in list:
    if task in row:
      list.remove(row)

while True:
  action = input("Do you want to add, view, edit or remove a to do? > ").strip().lower()
  if action == "add":
    add()
  elif action == "view":
    view()
  elif action == "edit":
    edit()
  elif action == "remove":
    remove()
  print()
  again = input("Do you want to see the menu again or quit? > ")
  os.system("clear")
  print()
  if again == "quit":
    break