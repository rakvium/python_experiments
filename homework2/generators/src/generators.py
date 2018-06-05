import json
import os

location = os.path.realpath(
    os.path.join(
        os.getcwd(), 'config.json'))

with open(location, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

print(data)
