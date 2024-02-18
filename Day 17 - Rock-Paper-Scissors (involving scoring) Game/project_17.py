from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E !")
player1_score = 0
player2_score = 0

print("Please choose your wepon: Rock(R), Paper(P) or Scissors(S)")

while True:
  print()
  player1 = input("Player 1 > ").upper()
  player2 = input("Player 2 > ").upper()
  print()
  
  if player1 in ["R","P", "S"] and player2 in ["R","P", "S"]:
    if player1 == "R" and player2 == "R" or player1 == "P" and player2 == "P" or player1 == "S" and player2 == "S":
      print("It's a tie!")
      continue
    elif player1 == "R" and player2 == "P" or player1 == "P" and player2 == "S" or player1 == "S" and player2 == "R":
      print("Score for Player 2!")
      player2_score += 1
    else:
      print("Score for Player 1!")
      player1_score += 1
  else:
    print("Invalid move! Try again!")
    continue
  if player1_score == 3:
    print("🏆 Player 1 wins the game! 🏆")
    break
  elif player2_score == 3:
    print("🏆 Player 2 wins the game! 🏆")
    break
    
print("Thanks for playing!")