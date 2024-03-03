import json

with open('file.json') as file:
    json_file = json.load(file)

print(json_file)
