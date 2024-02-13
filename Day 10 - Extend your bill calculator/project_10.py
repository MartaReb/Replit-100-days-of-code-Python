bill = float(input("What is the bill?: "))
tip = int(input("What % of the tip would you like to leave?: "))
bill_with_tip= tip / 100 * bill + bill
numberOfPeople = int(input("How many people?: "))
final_amount = bill_with_tip / numberOfPeople
final_amount = round(final_amount, 2)
print("You all owe", final_amount)