print("🌟Star Wars Name Generator🌟")
print()
first = input("Input your first name > ").strip().capitalize()
last = input("Input your lastname > ").strip().lower()
maiden = input("Input your mother's maiden name > ").strip().capitalize()
city = input("Input the city where you were born > ").strip().lower()

sliceFirst=first[0:3]
sliceLast=last[0:3]
newFirst = f"{sliceFirst}{sliceLast}"

sliceMaiden = maiden[0:2]
sliceCity = city[-3:]
newLast = f"{sliceMaiden}{sliceCity}"
print()
print(f"Your Star Wars name is {newFirst} {newLast}")