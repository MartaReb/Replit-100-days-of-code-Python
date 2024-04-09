import random, time, os
print("Idea Storage")
print()

def add():
  idea = input("Input your idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  print()
  print("Nice! Your idea has been stored.")
  time.sleep(2)
  os.system("clear")

def show():
  f = open("my.ideas", "r")
  ideas_list = f.read().split("\n")
  f.close()
  ideas_list.remove("")
  print(random.choice(ideas_list))
  time.sleep(2)
  os.system("clear")

while True:
  menu = input("Add an idea, see a random idea or quite? a/r/q > ")
  if menu == "a":
    add()
  elif menu == "r":
    show()
  elif menu == "q":
    break