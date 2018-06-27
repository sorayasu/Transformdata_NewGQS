import json
from functools import reduce
import requests
from flatten_json import unflatten_list

# def grouping(ds):
#     result = dict()
#     for k, v in ds.items():
#         if "__" in k:
#             attrs = k.split("__")
#             if attrs[0] not in result.keys():
#                 result[attrs[0]] = dict()
#             result[attrs[0]][attrs[1]] = v
#         else:
#             result[k] = v
#     return result

#result = list(map(grouping, data))
# print(json.dumps(result, indent=4, ensure_ascii=False))

# def convert_to_json(prev, current):
#     for i in prev:
#         # print("P -- ",prev[k], "C -- ",current[k])
#         if prev[i] != current[i]:
#             if type(prev[i]) is not list :
#                 temp = prev[i]
#                 prev[i] = list()
#                 prev[i].append(temp)
#                 prev[i].append(current[i])
#             else:
#                 if current[i] not in prev[i]:
#                     prev[i].append(current[i])
#                     #print("add +++++++++",prev[k])
#     return prev


def get_raw_patient_json(query):
    # print(query.json())
    # result = list(map(grouping, query.json()))
    # result = reduce(convert_to_json, result)
    # result = reduce(join_row, map(group_underscore_key, query))
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
    # print(unflatten_list(data, separator='__'))
    # print("+++++",data,"\n")
    data = addlist(unflatten_list(data, separator='__'))
    # print("*********",data)
    return data

# def grouping(prev, current):
#     mainkey = current[0].split('__')[0]
#     supportkey = current[0].split('__')[1]
#     if mainkey not in prev.keys():
#         prev[mainkey] = [{}]
#     prev[mainkey][0][supportkey] = current[1]
#     return prev

# def addobject(x, y):
#     (key, value) = y
#     x[key] = value
#     return x

# def items_to_dict(items):
#     return reduce(addobject, items, {})

# def group_underscore_key(row):
#     # print(row)
#     try:
#         data_with_underscore = filter(lambda item: "__" in item[0], row.items())
#         data_without_underscore = items_to_dict(filter(lambda item: "__" not in item[0], row.items()))
#         data_group = reduce(grouping, data_with_underscore, {})
#         return {**data_without_underscore, **data_group} # Join two dict
#     except Exception as e:
#         print("error",e)
#         result = {}
        # return result

def unionnest(fundamental,data):
    for v in data:
        for k,val in v.items():
            if type(val) is list:
                unionnest(fundamental,val)
                print("unionnest",k,"===",val)
                # if val not in fundamental['contained'][0]['code'][0][k]:
                #     print("___^__",val)
                #     # fundamental[key].append(value[0])
                #     print("_________",fundamental[k])
        return k,val
    # print("-------",val)
    


def union(fundamental, addkey):
    # print("fundamental+++++",fundamental)
    # print("addkey------",addkey)
    key, value = addkey
    unionnest(fundamental,value)
    if value[0] not in fundamental[key]:
        fundamental[key].append(value[0])
    return fundamental

def addlist(data):
    # print("add------",data)
    # print("data******  ",data)
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


def union(prev, current):
    # print(prev)
    # print("====",current)
    # for k,v in prev.items(),current.items():
        # print(k,v)
    # print("fundamental+++++",fundamental)
    # print("addkey------",addkey)
    # key, value = addkey
    # unionnest(fundamental,value)
    # if value[0] not in fundamental[key]:
    #     fundamental[key].append(value[0])
    return current

# def join_row(prev, current):
#     print(prev)
#     print("====",current)
#     # for k,v in prev.items():
#     #     print(type(k),    v)
#     return reduce(union, dataobject, prev)


# print(reduce(join_row, map(group_underscore_key, input_data)))
