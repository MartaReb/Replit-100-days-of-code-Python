print("🌟Current Leader🌟")
print()
print("Analyzing high scores......")
print()
f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

max_score = 0
name = ""

for row in scores:
  data = row.split()
  if data != []:
    if int(data[1]) > max_score:
      max_score = int(data[1])
      name = data[0]
              
print("Current leader is", name, "with", max_score, "scores.")