import random, time

def character():
  name = input("Name your Legend: ")
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  print()
  return name, type

def rollDice(sides):
  return random.randint(1,sides)

def health():
  healthStat = rollDice(6) * rollDice(12) / 2 + 10
  return healthStat

def strength():
  strengthStat = rollDice(6) * rollDice(8)/ 2 + 12
  return strengthStat 

while True:
  print("⚔️ BATTLE TIME ⚔️")
  (print)
  name1, type1 = character()
  print(name1)
  print(type1)
  health1 = health()
  print("HEALTH: ", health1)
  strength1 = strength()
  print("STRENGTH: ", strength1)
  print()
  print("Who are they battling?")
  print()
  name2, type2 = character()
  print(name2)
  print(type2)
  health2 = health()
  print("HEALTH: ", health2 )
  strength2 = strength()
  print("STRENGTH: ", strength2)
  time.sleep(3)
  print("⚔️ BATTLE TIME ⚔️")
  print("The battle begins!")
  time.sleep(5)
  print()
  round = 1
  
  while True:
    char1Dice = rollDice(6)
    char2Dice = rollDice(6)
    difference = abs(strength1 - strength2) + 1
    if char1Dice > char2Dice:
      health2 -= difference
      if round == 1:
        print(name1, "wins the first blow.")
      else:
        print(name1, "wins round", round)
        print(name2, "takes a hit, with", difference, "damage.")
    elif char1Dice < char2Dice:
      health1 -= difference
      if round == 1:
        print(name2, "wins the first blow")
      else:
        print(name2, "wins round", round)
        print(name1, "takes a hit, with", difference, "damage.")
    
    print()
    print(name1)
    print("HEALTH: ", health1)
    print()
    print(name2)
    print("HEALTH: ", health2)
    print()
  

    if health1 <= 0:
      print("Oh no!", name1 ,"has died!")
      print(name2,"destroyed", name1, "in", round, "rounds!")
      exit()
    elif health2 <= 0:
      print("Oh no", name2 ,"has died!")
      print(name1,"destroyed", name2, "in", round, "rounds!")
      exit()
    else:
      print("And they're both standing for the next round!")
      round += 1
      print()
      time.sleep(5)
      print("⚔️ BATTLE TIME ⚔️")
      print("The battle continues!") 
      print()

    time.sleep(5)