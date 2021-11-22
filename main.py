import pandas as pd
import csv
from operator import itemgetter


def expected_value(own_points, opponent_points):
    return 1 / (1 + 10**((opponent_points - own_points) / 400))


def new_ELO_points(old_points, k, s, e):
    """
   Returns new ELO points after match

   :param int old_points: The ELO points before the   match
   :param int k: The greater k, the greater the
    impact of newly achieved results. Is usually 20, for top players (Elo > 2400) 10, for less than 30 rated games 40, for youth players (under 18, Elo < 2300) 40.
   :param int s: Actual points scored by player (1 for each win, 0.5 for each draw, 0 for each loss)
   :param int e: Expected value
   :return: new ELO points
   :rtype: int
  """
    new_points = round(old_points + k * (s - e))
    return new_points


START_ELO = 1000
K = 40
df = pd.read_csv('input/matches.csv', header=[0])
df = df.sort_values(by=['date'])
players = {}
for index, row in df.iterrows():
    player1 = row['player1']
    player2 = row['player2']
    player1p = row['p1_points']
    player2p = row['p2_points']
    print("Match #" + str(index) + " - " + row['date'] + " - " + player1 +
          " vs. " + player2)
    # Add new players
    if player1 not in players:
        players[player1] = {
            "name": player1,
            "points": START_ELO,
            "wins": 0,
            "losses": 0,
            "ties": 0
        }
        print("New player " + player1 + " with " + str(START_ELO) + " points.")
    if player2 not in players:
        players[player2] = {
            "name": player2,
            "points": START_ELO,
            "wins": 0,
            "losses": 0,
            "ties": 0
        }
        print("New player " + player2 + " with " + str(START_ELO) + " points.")
    player1_elo = players[player1]["points"]
    player2_elo = players[player2]["points"]
    s_1, s_2 = 0, 0
    if player1p > player2p:
        s_1, s_2 = 1, 0
        players[player1]["wins"] += 1
        players[player2]["losses"] += 1
        print(player1 + " (" + str(player1_elo) + ") wins against " + player2 +
              " (" + str(player2_elo) + ").")
    elif player2p > player1p:
        s_2, s_1 = 1, 0
        players[player2]["wins"] += 1
        players[player1]["losses"] += 1
        print(player2 + " (" + str(player2_elo) + ") wins against " + player1 +
              " (" + str(player1_elo) + ").")
    else:
        s_1, s_2 = 0.5, 0.5
        players[player1]["ties"] += 1
        players[player2]["ties"] += 1
    players[player1]["points"] = new_ELO_points(
        player1_elo, K, s_1, expected_value(player1_elo, player2_elo))
    players[player2]["points"] = new_ELO_points(
        player2_elo, K, s_2, expected_value(player2_elo, player1_elo))
    print("New Points: " + player1 + " has " +
          str(players[player1]["points"]) + " and " + player2 + " " +
          str(players[player2]["points"]) + " points.\n")
players = sorted(players.values(), key=itemgetter("points"))
print("Rank - Name - ELO points - Wins - Ties - Losses")
for x in range(1, len(players) + 1):
    act_player = players[len(players) - x]
    print("#" + str(x) + " " + act_player["name"] + " - " +
          str(act_player["points"]) + " - " + str(act_player["wins"]) + " - " +
          str(act_player["ties"]) + " - " + str(act_player["losses"]))

with open('output/ranking.csv', 'w', newline='') as csvfile:
    fieldnames = ['rank', 'name', 'elo', 'wins', 'losses', 'ties']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in range(1, len(players) + 1):
        act_player = players[len(players) - x]
        writer.writerow({
            'rank': x,
            'name': act_player["name"],
            'elo': str(act_player["points"]),
            'wins': act_player["wins"],
            'losses': act_player["losses"],
            'ties': act_player["ties"]
        })
