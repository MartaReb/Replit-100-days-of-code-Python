print("Math Game!")
print()
user_number = int(input("Name your multiples: "))
score = 0

for i in range(1, 11):
  multiples = user_number * i
  print(i, "X",user_number,"=")
  user_answer = int(input())
  if user_answer == multiples:
    print("Great work!")
    score += 1
  else:
    print("Nope. The answer was", multiples)
    
print("---")
if score == 10:
  print("Wow 10/10 🥳! You are great at math!")
else:
  print("You scored", score, "out of 10 correct")