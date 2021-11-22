import pandas as pd


def expected_value(own_points, opponent_points):
    return 1 / (1 + 10**((opponent_points - own_points) / 400))


def new_ELO_points(old_points, k, s, e):
    """
   Returns new ELO points after match

   :param int old_points: The ELO points before the   match
   :param int k: The greater k, the greater the
    impact of newly achieved results. Is usually 20, for top players (Elo > 2400) 10, for less than 30 rated games 40, for youth players (under 18, Elo < 2300) 40.
   :param int s: Actual points scored by player (1    for each win, 0.5 for each draw, 0 for each loss)
   :param int e: Expected value
   :return: new ELO points
   :rtype: int
  """
    new_points = old_points
    return new_points


START_ELO = 1000
K = 20
df = pd.read_csv('input/matches.csv', header=[0])
df = df.sort_values(by=['date'])
players = {}
for index, row in df.iterrows():
    player1 = row['player1']
    player2 = row['player2']
    player1p = row['p1_points']
    player2p = row['p2_points']
    # Add new players
    if player1 not in players:
        players[player1] = START_ELO
    if player2 not in players:
        players[player2] = START_ELO
    player1_elo = players[player1]
    player2_elo = players[player2]
    s_1, s_2 = 0, 0
    if player1p > player2p:
        s_1, s_2 = 1, 0
    elif player2p > player1p:
        s_2, s_1 = 1, 0
    else:
        s_1, s_2 = 0.5, 0.5
    players[player1] = new_ELO_points(player1_elo, K, s_1,
                                      expected_value(player1_elo, player2_elo))
    players[player2] = new_ELO_points(player2_elo, K, s_2,
                                      expected_value(player2_elo, player1_elo))
print(players)
players = sorted(players.items(), key=lambda x: x[1])
for x in range(1, len(players) + 1):
    print(players[len(players) - x][0])
    print(players[len(players) - x][1])
