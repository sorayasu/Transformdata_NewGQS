import json
from functools import reduce
import requests
from flatten_json import unflatten_list

formatt_list = ['code','route','text','organization']
format_list_null = ['note']

def get_raw_diagnosis_json(query):
    try:
        result = reduce(join_row, map(flatten_json, query))
        # print(json.dumps(result, indent=4, ensure_ascii=False))
        # print(len(result))
    except Exception as e:
        print("error", e)
        result = {}
    return result.get('data')

def flatten_json(data):
    # print("1     ", data )
    # print("10    ",json.dumps(data))
    data = addlist(unflatten_list(data, separator='__'))
    # print("10    ",json.dumps(data))
    return data


def addlist(data):
    # print("2   ", data )
    for i, v in data.items():
        if type(v) is dict and i not in formatt_list:
            # print("v   ",i ,    v)
            addlist(v) 
            val = v
            data[i] = list()
            data[i].append(val)
        elif type(v) is dict and i in formatt_list:
                addlist(v) 
                data[i] = dict()
                data[i].update(v)
        elif i in format_list_null:
                data[i] = list()
    return data


def union(fundamental, addkey):
    key, value = addkey
    # print("000",  key)
    # print("key   ",fundamental[key])
    # print("00   ",fundamental['contained'][0]['code'])
    # print("value   ",value[0])
    # print("8   ",value[0]['code'])
    if value[0] not in fundamental[key]:
        fundamental[key].append(value[0])
    return fundamental

def join_row(prev, current):
    # print("curr   ",current.items())
    dataobject = filter(lambda item: isinstance(item[1], list), current.items())
    # print("list   ", list(dataobject))
    return reduce(union, dataobject, prev)

# result = get_raw_patient_json(data)
# print(json.dumps(result, indent=4, ensure_ascii=False))
# print(reduce(join_row, map(group_underscore_key, input_data)))