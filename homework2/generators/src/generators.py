import json
import os

location = os.path.realpath(
    os.path.join(
        os.getcwd(), 'config.json'))

with open(location, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

location = os.path.realpath(
    os.path.join(
        os.getcwd(), 'config_backup.env'))

backup = open(location, 'w')
if backup:
    for d in data:
        backup.write("".join(["%s=%s\n" % (k, str(v)) for k, v in d.items()]))
    backup.close()

if __name__ == "__main__":
    print(data)
