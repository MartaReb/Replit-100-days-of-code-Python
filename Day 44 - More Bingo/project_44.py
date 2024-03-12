import random
print("BINGO!")
print()

def randomNumber():
  number = random.randint(1,91)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()
  print()

def createCrad():
  numbers = []
  draw = 8
  while draw > 0:
    number = randomNumber()
    if number not in numbers:
      numbers.append(number)
      draw -=1
  
  numbers.sort()
  
  global bingo
  bingo = [[ numbers[0], numbers[1], numbers[2]],
  [ numbers[3], "BINGO!", numbers[4] ],
  [ numbers [5], numbers[6], numbers[7]]]

createCrad()

exes = 0
while True:
  prettyPrint()
  userNumber = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == userNumber:
        bingo[row][item] = "X"
        exes +=1
    if exes == 8:
      print("You have won!")
      break