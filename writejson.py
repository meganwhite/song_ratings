import csv
import json

#read csv
with open('song_list.csv',) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#write json
with open('song_list.json', 'w') as f:
    json.dump(rows, f, indent=2)