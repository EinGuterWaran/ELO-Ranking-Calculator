import csv
with open('input/matches.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in spamreader:
    print(', '.join(row))
