from flatten_json import unflatten_list
import json
from functools import reduce
import requests
from flatten_json import flatten, unflatten, unflatten_list

formatt_list = ['coding','route','text','organization',]
config = {"check_med" : "contained__code__coding__code","group_med" : "contained__route__coding"}


data = [
    {
        "context": "I02-17-000021",
        "subject": "02-17-000025",
        "status_system": "TC",
        "status_code": None,
        "status_display": None,
        "identifiers__system": "TC",
        "identifiers__type": "OEORD_RowId",
        "identifiers__use": "official",
        "identifiers__value": "9251815",
        "contained__resource_type": "Medication",
        "contained__ingredient__coding__system": "TC",
        "contained__ingredient__coding__code": 1075,
        "contained__ingredient__coding__display": "Alcohol",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "51102707000059",
        "contained__code__coding__display": "Handi-C Hand Rub SOLUTION (240mL)",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "4",
        "contained__route__coding__display": "Topical",
        "contained__method": None,
        "contained__instruction_text": "Handi-C Hand Rub SOLUTION (240mL)",
        "contained__instruction_text_local": None,
        "info_status_system": "TC",
        "info_status_code": "V",
        "info_status_display": "Verified",
        "patient_instruction": None,
        "quantity": 1,
        "dose_quantity": "1"
    },
    {
        "context": "I02-17-000021",
        "subject": "02-17-000025",
        "status_system": "TC",
        "status_code": None,
        "status_display": None,
        "identifiers__system": "TC",
        "identifiers__type": "OEORD_RowId",
        "identifiers__use": "official",
        "identifiers__value": "9251815",
        "contained__resource_type": "Medication",
        "contained__ingredient__coding__system": "TC",
        "contained__ingredient__coding__code": 539,
        "contained__ingredient__coding__display": "Oxytetracycline (Oxylim)",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "MEETERR0000O",
        "contained__code__coding__display": "Terramycin Eye-Ointment ",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "35",
        "contained__route__coding__display": "Ophthalmic",
        "contained__method": None,
        "contained__instruction_text": "(Do Not Use After Opening 1 Month)",
        "contained__instruction_text_local": "ไม่เก็บยาไว้เกิน 1 เดือน หลังเปิดขวดใช้แล้ว",
        "info_status_system": "TC",
        "info_status_code": "E",
        "info_status_display": "Executed",
        "patient_instruction": None,
        "quantity": 1,
        "dose_quantity": "1"
    },
    {
        "context": "I02-17-000021",
        "subject": "02-17-000025",
        "status_system": "TC",
        "status_code": None,
        "status_display": None,
        "identifiers__system": "TC",
        "identifiers__type": "OEORD_RowId",
        "identifiers__use": "official",
        "identifiers__value": "9251815",
        "contained__resource_type": "Medication",
        "contained__ingredient__coding__system": "TC",
        "contained__ingredient__coding__code": 2453,
        "contained__ingredient__coding__display": "Phytomenadione (vit K1)",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "MIVKONA0002O",
        "contained__code__coding__display": "Konakion mm (2 Mg) Ped Inj.(vit K)(**)",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "3",
        "contained__route__coding__display": "Intravenous",
        "contained__method": None,
        "contained__instruction_text": "Can use :IV, IM,ORAL",
        "contained__instruction_text_local": "Can use :IV, IM,ORAL",
        "info_status_system": "TC",
        "info_status_code": "E",
        "info_status_display": "Executed",
        "patient_instruction": None,
        "quantity": 1,
        "dose_quantity": "0.5"
    }
]

def get_raw_patient_json(query):
    try:
        # raw_data = groupping(query)
        # print("gropping ",raw_data)
        # result = reduce(join_row, map(flatten_json, raw_data))
        result = reduce(join_row, map(flatten_json, query))
    except Exception as e:
        print("error", e)
        result = {}
    return result

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
    return data


def union(fundamental, addkey):
    key, value = addkey
    # print("000",  key)
    # print("key   ",fundamental[key])
    # print("00   ",fundamental['contained'][0]['code'])
    print("value   ",value[0])
    # print("8   ",value[0]['code'])
    if type(value[0]) is dict or type(value[0]) is list :
        print("eieiei")
        print("fundamental     ",fundamental[key])
        # dataobject = filter(lambda item: isinstance(item[1], list), fundamental[0][key])
        if value[0] not in fundamental[key]:
            union(value[0],fundamental[key])
            print(dataobject)
        # reduce(union, value[0], fundamental[key])
    # if value[0] not in fundamental[key]:
    #     fundamental[key].append(value[0])
    # return fundamental

def join_row(prev, current):
    # print("curr   ",current.items())
    dataobject = filter(lambda item: isinstance(item[1], list), current.items())
    # print("list   ", list(dataobject))
    return reduce(union, dataobject, prev)
result = get_raw_patient_json(data)
# print(json.dumps(result, indent=4, ensure_ascii=False))