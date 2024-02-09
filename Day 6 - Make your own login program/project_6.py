print("Secure Login")
print("--"*6)
name = input("What's your name? ")
password = input("What's your password? ")

if name == "John" and password == "admin1":
  print("Hello John!")
elif name == "Janne" and password == "admin2":
  print("Welcom Janne!")
elif name == "David" and password == "admin3":
  print("Hi David!")
else:
  print("You don't have an account here...sorry!")