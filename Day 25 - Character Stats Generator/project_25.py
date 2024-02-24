import random 
print("⚔️ Character Stats Generator ⚔️")
print()
def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

makeCharacter = "yes"
while makeCharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is: ", health, "hp")
  makeCharacter = input("Want to create another character? ")
  print()