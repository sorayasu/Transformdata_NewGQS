import json
from functools import reduce
import requests
from flatten_json import unflatten_list

formatt_list = ['code','route','text','organization']
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
        "contained__ingredient__coding__code": 1549,
        "contained__ingredient__coding__display": "General",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "MXXSYRT0001O",
        "contained__code__coding__display": "Syringe 1 Ml Terbuculin (Disp.)",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "42",
        "contained__route__coding__display": "Miscellaneous",
        "contained__method": None,
        "contained__instruction_text": "Syringe 1 Ml Terbuculin (Disp.)",
        "contained__instruction_text_local": "Syringe 1 Ml Terbuculin (Disp.)",
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
        "contained__ingredient__coding__code": 1549,
        "contained__ingredient__coding__display": "General",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "24122002000007",
        "contained__code__coding__display": "Milk Bottle 4 Oz (NEW)",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "1",
        "contained__route__coding__display": "Oral",
        "contained__method": None,
        "contained__instruction_text": None,
        "contained__instruction_text_local": None,
        "info_status_system": "TC",
        "info_status_code": "V",
        "info_status_display": "Verified",
        "patient_instruction": "\"1  ขวด; as directed :ตามแพทย์สั่ง, \"",
        "quantity": 2,
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
        "contained__ingredient__coding__code": 1473,
        "contained__ingredient__coding__display": "Ethyl alcohol",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "MELALCO2070L",
        "contained__code__coding__display": "Alcohol 70% Sol (60ml)",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "4",
        "contained__route__coding__display": "Topical",
        "contained__method": None,
        "contained__instruction_text": None,
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
        "contained__ingredient__coding__code": 1170,
        "contained__ingredient__coding__display": "BCG Vaccine",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "MRIBCGI0000L",
        "contained__code__coding__display": "B.C.G.Vaccine",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "20",
        "contained__route__coding__display": "Intradermal",
        "contained__method": None,
        "contained__instruction_text": "Keep in refrigerator (2 - 8 C)/Can use : ID only",
        "contained__instruction_text_local": "เก็บยาในตู้เย็น (2 - 8 C)/Can use : ID only",
        "info_status_system": "TC",
        "info_status_code": "E",
        "info_status_display": "Executed",
        "patient_instruction": "\"1  Dose; prn :เวลามีอาการ, \"\r\nฉีดเข้าชั้นผิวหนัง (ID) ครั้งละ",
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
        "contained__ingredient__coding__code": 1549,
        "contained__ingredient__coding__display": "General",
        "contained__code__coding__system": "TC",
        "contained__code__coding__code": "MXXSYRT0001O",
        "contained__code__coding__display": "Syringe 1 Ml Terbuculin (Disp.)",
        "contained__from": None,
        "contained__route__coding__system": "TC",
        "contained__route__coding__code": "42",
        "contained__route__coding__display": "Miscellaneous",
        "contained__method": None,
        "contained__instruction_text": "Syringe 1 Ml Terbuculin (Disp.)",
        "contained__instruction_text_local": "Syringe 1 Ml Terbuculin (Disp.)",
        "info_status_system": "TC",
        "info_status_code": "V",
        "info_status_display": "Verified",
        "patient_instruction": None,
        "quantity": 1,
        "dose_quantity": "1"
    }
]

def get_raw_medication_json(query):
    try:
        raw_data = groupping(query)
        # print("gropping ",raw_data)
        # result = reduce(join_row, map(flatten_json, raw_data))
        result = reduce(join_row, map(flatten_json, raw_data))
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
            if data[i][config['check_med']] == data[i+1][config['check_med']]:
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
                        d = {config['group_med']+"__"+str(i)+x[1]:data[i][k]}
                        l = {config['group_med']+"__"+str(i+1)+x[1]:data[i+1][k]}
                        raw_data.update(d)
                        raw_data.update(l)
                raw_json.append(raw_data)
            else: raw_json.append(data[i+1])
        # print(raw_json)
        return raw_json
    except Exception as e:
        print("error", e)
        return data
    

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

# result = get_raw_medication_json(data)
# print(json.dumps(result, indent=4, ensure_ascii=False))
# print(reduce(join_row, map(group_underscore_key, input_data)))