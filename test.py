f= open("games.pgn", "r")
dane = f.readlines()
f.close()
print(dane[:50])