
import json


def data_to_json(data: tuple):
    return_json = {}
    for line in data:
        return_json[line[0]] = line[1]
    return json.dumps(return_json)
