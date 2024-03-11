import random

def randomNumber():
  number = random.randint(0,90)
  return number

numbers = []
draw = 8
while draw > 0:
  number = randomNumber()
  if number not in numbers:
    numbers.append(number)
    draw -= 1

numbers.sort()

bingo = [[ numbers[0], numbers[1], numbers[2]],
  [ numbers[3], "BINGO!", numbers[4] ],
  [ numbers [5], numbers[6], numbers[7]]]

for row in bingo:
  print(row)