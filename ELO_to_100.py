import csv  
import random
filename = "ELO_to_100"
how_many_players = 100
how_many_matches = 1000000

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
        #2900er Elo: 
        # bei 0,85-1,15: 87,5 
        # bei 0,88-1,12: 79
        # bei 0,80-1,20: ü100
        # bei 0,82-1,18: 98,5
        # bei 0,83-1,17:  93,5
      data = ['01.01.2021', players[player1][0], players[player2][0],random.randint(int(players[player1][1]*0.83),int(players[player1][1]*1.17)), 
              random.randint(int(players[player2][1]*0.83),int(players[player2][1]*1.17))]
      print(a+1)
      writer.writerow(data)
    print(players)

