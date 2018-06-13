import json
import os

location = os.path.realpath(
    os.path.join(
        os.getcwd(), 'config.json'))

with open(location, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

print(data)

location = os.path.realpath(
    os.path.join(
        os.getcwd(), 'config_backup.env'))

backup = open(location, 'w')

dict_list = data
for values in dict_list:
    backup.write("".join(["%s=%s\n" % (k, str(v)) for k, v in values.items()]))
