from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E !")

print("Please choose your wepon: Rock(R), Paper(P) or Scissors(S)")
print()
player1 = input("Player 1 > ").upper()
print()
player2 = input("Player 2 > ").upper()
print()

if player1 in ["R","P", "S"] and player2 in ["R","P", "S"]:
  if player1 == "R" and player2 == "R" or player1 == "P" and player2 == "P" or player1 == "S" and player2 == "S":
    print("It's a tie!")
  elif player1 == "R" and player2 == "P" or player1 == "P" and player2 == "S" or player1 == "S" and player2 == "R":
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
else:
  print("Invalid move! Try again!")