import csv, os

with open ("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    dir_list = os.listdir()
    artist = row["Artist(s)"]
    if artist not in dir_list:
      os.mkdir(artist)
    song = row["Song"]
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()