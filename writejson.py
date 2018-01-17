import csv
import json

#read csv
with open('song_list.csv',) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

def remove_quotes(csv_data):
	for row in csv_data:
		row['Song'] = row['Song'].replace('"','')
		row['Year'] = int(row['Year'])
	return csv_data


new_csv = remove_quotes(rows)


#write json
with open('song_list.json', 'w') as f:
    json.dump(new_csv, f, indent=2)