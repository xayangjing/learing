import json


f = open('Jason_test', 'r')

data = f.read()

data = json.loads(data)

print(data['name'])