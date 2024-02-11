print ("Are you a superfan of 'Friends' or a fake fan?")
print("Answer these questions to find out.")
print()
question1=input("How many times did Ross get married? ")
if question1=="3":
  print("Correct!")
else:
  question2 = input("Are you sure (yes/no)? ")
  if question2 == "yes":
    print("Wrong!")
  elif question2 == "no":
    print("The right answer is 3.")