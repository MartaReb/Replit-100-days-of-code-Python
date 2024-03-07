import random

print("🥦 Veggy-Hangman 🥦")
listOfVeggy = ["carrot", "potato", "tomato", "onion", "lettuce", "cucumber", "pepper", "broccoli", "spinach", "garlic", "cabbage", "zucchini", "cauliflower", "pea", "bean", "corn", "radish", "eggplant", "celery"]
word = random.choice(listOfVeggy)

letterPicked = []

lives = 6
while lives > 0:
  userLetter = input("\n\nChoose a letter: ").lower()
  
  if userLetter in letterPicked:
    print("You've tried that before.")
    continue
  else:
    letterPicked.append(userLetter)
    
  if userLetter in word:
    print("Correct!")
  else:
    print("Nope, not in there.")
    lives -= 1
    if lives == 0:
      print(f"\nYou ran out of lives! The answer was {word}.")
      break
    else:
      print(f"You have {lives} lives left.")

  allLetters = True
  for l in word:
    if l in letterPicked:
      print(l, end="")
    else:
      print("_", end="")
      allLetters = False

  if allLetters:
    print(f"\n\nThis is our word! You won with {lives} left!")
    break