import csv
import json

data = []

with open('table.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        name = row['English'].split('.')[0]
        jsonObject = {
            "name": name,
            "label": {
                "FR": row['French'],
                "EN": row['English'],
                "DE": ""
            },
            "img_src": f"C:\\DevOps\\SmartHomeModel\\designer-digitalhome-cloud\\symbols\\{row['English']}"
        }
        data.append(jsonObject)

with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)
