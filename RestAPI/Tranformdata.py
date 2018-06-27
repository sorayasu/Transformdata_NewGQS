import json
from functools import reduce
import requests
from flatten_json import unflatten_list

def get_raw_patient_json(query):
    try:
        result = reduce(join_row, map(flatten_json, query))
        # result = reduce(join_row, map(group_underscore_key, query))
    except Exception as e:
        print("error", e)
        result = {}
        return result
    # print(unflatten_list(query))
    return (result)


def flatten_json(data):
    data = addlist(unflatten_list(data, separator='__'))
    return data

# def unionnest(fundamental,data):
#     for v in data:
#         for k,val in v.items():
#             if type(val) is list:
#                 unionnest(fundamental,val)
#                 print("unionnest",k,"===",val)
#                 # if val not in fundamental['contained'][0]['code'][0][k]:
#                 #     print("___^__",val)
#                 #     # fundamental[key].append(value[0])
#                 #     print("_________",fundamental[k])
#         return k,val
#     # print("-------",val)
    


def union(fundamental, addkey):
    key, value = addkey
    if value[0] not in fundamental[key]:
        fundamental[key].append(value[0])
    return fundamental

def addlist(data):
    for i, v in data.items():
        if type(v) is dict:
            addlist(v) 
            # print(v)
            val = v
            data[i] = list()
            data[i].append(val)
    return data

def join_row(prev, current):
    dataobject = filter(lambda item: isinstance(item[1], list), current.items())
    return reduce(union, dataobject, prev)


# print(reduce(join_row, map(group_underscore_key, input_data)))
