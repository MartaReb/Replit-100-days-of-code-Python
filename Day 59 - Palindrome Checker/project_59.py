print("Palindrome Checker")
print()

def palindrome(word):
  if len(word) <= 1:
    return True
  elif word[0] != word[-1]:
    return False
  else:
      return palindrome(word[1:-1]) 

user_word = input("Input a word > ")
word = user_word.replace(" ", "").lower()
if palindrome(word):
  print(f"{user_word} is a palindrome.")
else:
  print(f"{user_word} is not a palindrome.")