print("Factorial Finder")

def factorial(number):
  if number == 1:
    return 1
  else:
    return number * factorial(number - 1)
 
number = int(input("Input a number > "))
print(factorial(number))