import json
from functools import reduce
import requests
from flatten_json import unflatten_list

formatt_list = ['code','route','text','organization']
check_med = "contained__code__coding__code"
group_med = "contained__route__coding"

# data = [
#     {
#         "context": "I02-17-000020",
#         "subject": "02-17-000023",
#         "status_system": "TC",
#         "status_code": None,
#         "status_display": None,
#         "identifiers__system": "TC",
#         "identifiers__type": "OEORD_RowId",
#         "identifiers__use": "official",
#         "identifiers__value": "9251829",
#         "contained__resource_type": "Medication",
#         "contained__ingredient__coding__system": "TC",
#         "contained__ingredient__coding__code": 1075,
#         "contained__ingredient__coding__display": "Alcohol",
#         "contained__ingredient__text": "Alcohol",
#         "contained__code__coding__system": "TC",
#         "contained__code__coding__code": "51102707000059",
#         "contained__code__coding__display": "Handi-C Hand Rub SOLUTION (240mL)",
#         "contained__code__text": "Handi-C Hand Rub SOLUTION (240mL)",
#         "contained__from": None,
#         "contained__route__coding__system": "TC",
#         "contained__route__coding__code": "4",
#         "contained__route__coding__display": "Topical",
#         "contained__route__text": "Topical",
#         "contained__method": None,
#         "contained__instruction_text": "Handi-C Hand Rub SOLUTION (240mL)",
#         "contained__instruction_text_local": None,
#         "info_status_system": "TC",
#         "info_status_code": "V",
#         "info_status_display": "Verified",
#         "patient_instruction": None,
#         "quantity": 1,
#         "dose_quantity": "1"
#     }
#     , {
#         "context": "I02-17-000020",
#         "subject": "02-17-000023",
#         "status_system": "TC",
#         "status_code": None,
#         "status_display": None,
#         "identifiers__system": "TC",
#         "identifiers__type": "OEORD_RowId",
#         "identifiers__use": "official",
#         "identifiers__value": "9251829",
#         "contained__resource_type": "Medication",
#         "contained__ingredient__coding__system": "TC",
#         "contained__ingredient__coding__code": 1075,
#         "contained__ingredient__coding__display": "Alcohol",
#         "contained__ingredient__text": "Alcohol",
#         "contained__code__coding__system": "TC",
#         "contained__code__coding__code": "51102707000059",
#         "contained__code__coding__display": "Handi-C Hand Rub SOLUTION (240mL)",
#         "contained__code__text": "Handi-C Hand Rub SOLUTION (240mL)",
#         "contained__from": None,
#         "contained__route__coding__system": "BCONN",
#         "contained__route__coding__code": "TOPI",
#         "contained__route__coding__display": "Topical",
#         "contained__route__text": "Topical",
#         "contained__method": None,
#         "contained__instruction_text": "Handi-C Hand Rub SOLUTION (240mL)",
#         "contained__instruction_text_local": None,
#         "info_status_system": "TC",
#         "info_status_code": "V",
#         "info_status_display": "Verified",
#         "patient_instruction": None,
#         "quantity": 1,
#         "dose_quantity": "1"
#     }
#     ,   {
#         "context": "I02-17-000020",
#         "subject": "02-17-000023",
#         "status_system": "TC",
#         "status_code": None,
#         "status_display": None,
#         "identifiers__system": "TC",
#         "identifiers__type": "OEORD_RowId",
#         "identifiers__use": "official",
#         "identifiers__value": "9251829",
#         "contained__resource_type": "Medication",
#         "contained__ingredient__coding__system": "TC",
#         "contained__ingredient__coding__code": 539,
#         "contained__ingredient__coding__display": "Oxytetracycline (Oxylim)",
#         "contained__ingredient__text": "Oxytetracycline (Oxylim)",
#         "contained__code__coding__system": "TC",
#         "contained__code__coding__code": "MEETERR0000O",
#         "contained__code__coding__display": "Terramycin Eye-Ointment ",
#         "contained__code__text": "Terramycin Eye-Ointment ",
#         "contained__from": None,
#         "contained__route__coding__system": "TC",
#         "contained__route__coding__code": "35",
#         "contained__route__coding__display": "Ophthalmic",
#         "contained__route__text": "Ophthalmic",
#         "contained__method": None,
#         "contained__instruction_text": "(Do Not Use After Opening 1 Month)",
#         "contained__instruction_text_local": "",
#         "info_status_system": "TC",
#         "info_status_code": "E",
#         "info_status_display": "Executed",
#         "patient_instruction": None,
#         "quantity": 1,
#         "dose_quantity": "1"
#     }
#     ]


# def transform_rawjson(data):
#     raw_json = {}
#     d = {}
#     i = 0
#     for d in data:
#         for k,val in d.items():
#             for s in formatt:
#                 # print("k  " , k,"s    ",s)
#                 if s in k:
#                     x = k.split(s)
#                     k = s +"__"+str(i)+x[1]
#                     d = {k:val}
#                     raw_json.update(d)
#             d = {k:val}
#             raw_json.update(d)                
#         i = i+1
#     # print(raw_json)
#     data = unflatten_list(raw_json, separator='__')
#     print(json.dumps(data))
#     return json.dumps(data)

# transform_rawjson(data)

def get_raw_patient_json(query):
    try:
        raw_data = groupping(query)
        print(raw_data)
        result = reduce(join_row, map(flatten_json, raw_data))
        # result = reduce(join_row, map(flatten_json, raw_data))
    except Exception as e:
        print("error", e)
        result = {}
    return result

def groupping(data):
    try:
        raw_json = [data[0]]
        raw_data = {}
        d = l ={}
        # print("groupping",   raw_json)
        for i in range(len(data)-1):
            if data[i][check_med] == data[i+1][check_med]:
                raw_json.pop()
                # print("raw   ", raw_json)
                for k,val in data[i].items():
                    if data[i][k] == data[i+1][k] and group_med not in k:
                        raw_data.update({k:val})
                        # print("raw_data    ", raw_data)
                    elif group_med in k :
                        # print("else    ",k)
                        x = k.split(group_med)
                        # print(" 1 ",x)
                        d = {group_med+"__"+str(i)+x[1]:data[i][k]}
                        l = {group_med+"__"+str(i+1)+x[1]:data[i+1][k]}
                        raw_data.update(d)
                        raw_data.update(l)
                raw_json.append(raw_data)
            else: raw_json.append(data[i+1])
        # print(raw_json)
        return raw_json
    except Exception as e:
        print("error", e)
        return data
    
#             for s in formatt:
#                 # print("k  " , k,"s    ",s)
#                 if s in k:
#                     x = k.split(s)
#                     k = s +"__"+str(i)+x[1]
#                     d = {k:val}
#                     raw_json.update(d)
#             d = {k:val}
#             raw_json.update(d)    
        # print("if")
        # print(data[0][check_med])
        # print("*******",data[i][check_med])
        # a = check_med.pop()
        # print("a    ",a)
        # print("a    ",data[i][check_med])
        # if data[i] in check_med:
        #     print(data[i].value)
        #     print(data[i])
    #     a = data.pop(i)
        # print("i   ",i)

def flatten_json(data):
    data = addlist(unflatten_list(data, separator='__'))
    return data


def addlist(data):
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
                # print("eiei   ",i ,    v)
    # print("1   ",data)
    return data


def union(fundamental, addkey):
    key, value = addkey
    # print("000",  addkey)
    # print("key   ",fundamental[key])
    # print("00   ",fundamental['contained'][0]['code'])
    # print("value   ",value[0])
    # print("8   ",value[0]['code'])
    if value[0] not in fundamental[key]:
        # # print("8   ",value[0]['code']['coding'])
        # try:
        #     if fundamental['contained'][0]['code']['coding'][0]['code'] == value[0]['code']['coding'][0]['code']:
        #     # group(fundamental,value[0])
        #     # print("5   ",fundamental[key])
        #     # print("6   "group(fundamental,value[0]))
        #     # print("7   ",group(fundamental,value[0]))
        #         fundamental[key] = [group(fundamental,value[0])]
        #     # print("test    ",json.dumps(fundamental, indent=4, ensure_ascii=False))
        #         return fundamental
        # except Exception as e:
        #     pass
        #     # print("equ   ",fundamental[key])
        # else : 
        #     print("eieiei")
        fundamental[key].append(value[0])
            # print("else    else",fundamental)
        # a = fundamental['contained'][0]['code'][0]['coding'][0]['code']
        # print(value[0]['code'][0]['coding'][0]['code'])
        # b = fundamental['contained'][0]['code'][0]['coding'][0]['code']
        # print(json.dumps(reduce(dict.get, config, fundamental)))
        # fundamental[key].append(value[0])
    # print("resu        ",fundamental)
    return fundamental

def join_row(prev, current):
    # print(current.items())
    dataobject = filter(lambda item: isinstance(item[1], list), current.items())
    # print("list   ", list(dataobject))
    return reduce(union, dataobject, prev)

# result = get_raw_patient_json(data)
# print(json.dumps(result, indent=4, ensure_ascii=False))
# print(reduce(join_row, map(group_underscore_key, input_data)))

# def test(data):
#     # print(data['contained'])
#     print(json.dumps(reduce(dict.get, config, data)))

# test(dataa)