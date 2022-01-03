import csv  
import random
filename = "ELO_to_100"
how_many_players = 100
how_many_matches = 200000

players = []
for x in range(1,how_many_players+1):
  players.append([str(x),x])
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

