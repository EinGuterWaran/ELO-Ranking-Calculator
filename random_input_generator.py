import csv
import random
from py_random_words import RandomWords

rnd_word = RandomWords()

filename = input("Enter a filename:\n")
how_many_players = int(input("How many players?\n"))
how_many_matches = int(input("How many matches?\n"))

players = []
for x in range(0, how_many_players):
    while True:
        new_name = rnd_word.get_word() + "-" + rnd_word.get_word()
        if new_name not in players:
            strength = random.randint(1, 1001)
            players.append([new_name+" ("+str(strength)+")", strength])
            break
with open('input/' + filename + '.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(['date', 'player1', 'player2', 'p1_points', 'p2_points'])

    # write the data
    for a in range(0, how_many_matches):
        player1 = random.randint(0, how_many_players - 1)
        player2 = random.randint(0, how_many_players - 1)
        while player2 == player1:
            player2 = random.randint(0, how_many_players - 1)
        data = ['01.01.2021', players[player1][0], players[player2][0],random.randint(int(players[player1][1]*0.83),int(players[player1][1]*1.17)), 
              random.randint(int(players[player2][1]*0.83),int(players[player2][1]*1.17))]
        print(a + 1)
        writer.writerow(data)
    print(players)
