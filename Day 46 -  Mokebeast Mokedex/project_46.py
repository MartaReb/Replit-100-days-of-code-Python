print("🌟MokeBeast Generator🌟")
print()

mokadex = {}

def prettyPrint():
  for key, value in mokadex.items():
    print(key, end="\n")
    for subKey, subValue in value.items():
      print(subKey, subValue, sep=": ", end=" | ")
    print()
    print()
    
while True:
  name = input("Input the beast name > ").title()
  element = input("Input the beast element > ").title()
  move = input("Input the beast special move > ").title()
  hp = input("Input the beast starting HP > ")
  mp = input("Input the beast starting MP > ")
  mokeBeast = {"Element": element, "Move": move, "HP": hp, "MP": mp}
  mokadex[name] = mokeBeast
  
  again = input("Again? y/n > ")
  print()
  if again == "n":
    break
prettyPrint()