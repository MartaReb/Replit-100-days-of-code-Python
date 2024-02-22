print("Replit Login System")
print()
def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "Marta" and password == "Python":
      print("Welcome Marta!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue
login()