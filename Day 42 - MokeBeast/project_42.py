print("👾 MokéBeast 👾")
print()

mokeBeast = {"Beast Name":None, "Type":None, "Special Move":None, "HP":None, "MP":None}

for name, value in mokeBeast.items():
  mokeBeast[name] = input(f"{name}: ").strip().title()
print()
if mokeBeast["Type"]=="Earth":
  print("\033[32m", end="")
elif mokeBeast["Type"]=="Air":
  print("\033[35m", end="")
elif mokeBeast["Type"]=="Fire":
  print("\033[31m", end="")
elif mokeBeast["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")
  
for name, value in mokeBeast.items():
  print(f"{name:<15}: {value}")