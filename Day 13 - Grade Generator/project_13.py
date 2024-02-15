print("Exam Grade Calculator")
print()
test_name = input("Enter the name of the test: ")
max_score = int(input("Enter the maximum score: "))
score = int(input("Enter the score received: "))
print()
percentage = int((round((score / max_score), 2)) * 100)

print("You got", percentage, "% on", test_name)
if percentage >= 90:
  print("You got an A+")
elif percentage >= 80:
  print("You got an A")
elif percentage >= 70:
  print("You got an B")
elif percentage >= 60:
  print("You got an C")
elif percentage >= 50:
  print("You got an D")
elif percentage <= 49:
  print("You got an U")
else: 
  print("Try again!")