# Elo-Ranking-Calculator
Calculates an ELO ranking from a CSV file with matches

## How to use this tool
1. Put a CSV file with the matches as described below into the input folder.
2. Start main.py and follow the instructions in the command line.
3. In the output folder you will now find a CSV file with the ranking, including ELO points, number of wins, draws and losses.

### Input: CSV file 
Header: date,player1,player2,p1_points,p2_points
- date: The date of the match. The format is important: YYYY-MM-DD. This Tool will sort the matches by the dates.
- player1, player2: Names of the players. The name has to be unique because it is also used as an identifier.
- p1_points, p2_points: The points/goals/... the players got in this match. If there is nothing like this in your use case just give the winner more points 
and if it's a tie give them both the same amount of points. The difference does not matter for the ELO.

### Example input files
You find two example files in the input folder. One are German battle rap matches of BMCL from "Rap am Mittwoch", 
[which can be found on Wikipedia](https://de.wikipedia.org/w/index.php?title=Rap_am_Mittwoch#Begegnungen_der_BMCL) and the other are fantasy footbal games I made up.
