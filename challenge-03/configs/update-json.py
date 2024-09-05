import csv
import json

with open('input.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    json_data = [row for row in csv_reader]

with open('config.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)