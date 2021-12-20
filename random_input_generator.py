import csv  
import random
import string
filename = input("Enter a filename:\n")
how_many_players = int(input("How many players?\n"))
how_many_matches = int(input("How many matches?\n"))

players = []
for x in range(0,how_many_players):
  new_name = ""
  name_len = random.randint(4,11)
  while True:
    for le in range(0,name_len):
      new_name += random.choice(string.ascii_letters)
    if new_name not in players:
      strength = random.randint(1,1001)
      players.append([new_name,strength])
      break
with open('input/'+filename+'.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(['date', 'player1', 'player2', 'p1_points', 'p2_points'])

    # write the data
    for a in range(0,how_many_matches):
      player1 = random.randint(0,how_many_players-1)
      player2 = random.randint(0,how_many_players-1)
      while player2 == player1:
        player2 = random.randint(0,how_many_players-1)
      data = ['01.01.2021', players[player1][0], players[player2][0],players[player1][1], players[player2][1]]
      print(a+1)
      writer.writerow(data)
    print(players)

