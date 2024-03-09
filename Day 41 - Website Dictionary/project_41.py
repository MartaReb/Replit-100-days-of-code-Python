print("🌟Website Rating🌟")
print()
name = input("Input the website name: ")
url = input("Input the URL: ")
description = input("Input your a description: ")
stars = input("Input the a star rating out of 5: ")
print()
websiteInfo = {"name":name, "url":url, "description" :description, "stars":stars}

for name, value in websiteInfo.items():
  print(f"{name}: {value}")