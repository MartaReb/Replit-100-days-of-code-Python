print("🌟Current Leader🌟")
print()
print("Analyzing high scores......")
f = open("high.score", "r")
list_of_scores = []
list_of_users = []
while True:
  contents = f.readline().strip()

  if contents == "":
    break
  user, score = contents.split() 
  list_of_scores.append(int(score))
  list_of_users.append(user)
  
  print(f"Current leader is {user}." )

f.close()