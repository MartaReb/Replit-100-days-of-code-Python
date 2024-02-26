import random, time, os

def character():
  name = input("Name your Legend: ")
  type = input("Character Type (human, elf, wizard, orc): ")
  print()
  return name, type

def rollDice(sides):
  return random.randint(1,sides)
  
def health():
  health = rollDice(6) * rollDice(12) / 2 + 10
  return int(health)

def strength():
  strength = rollDice(6) * rollDice(12)/ 2 + 12
  return int(strength)

while True:
  print("Character Builder")
  name, type = character()
  print(name)
  print(type)
  print("HEALTH: ", health())
  print("STRENGTH: ", strength())
  print("May your name go down in Legend...")
  print()
  time.sleep(1)
  again = input("Do you want to create another character? ")
  print()
  if again == "no" or again == "No":
    break
    time.sleep(1)
    os.system("clear")