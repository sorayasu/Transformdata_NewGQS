from flatten_json import unflatten_list
import json
from functools import reduce
import requests
from flatten_json import flatten, unflatten, unflatten_list

formatt_list = ['coding','route','text','organization',]
config = {"check_med" : "contained__code__coding__code","group_med" : "contained__route__coding"}


data = [
    {
        "severity": None,
        "body_site": "None",
        "asserted_date": "2014-10-01 13:00:29.783",
        "patient": "48-14-000019",
        "encounter": "O48-14-000010",
        "clinical_status": None,
        "verification_status": "unknown",
        "asserter": "048140334",
        "code__coding__code": "Z00.0",
        "code__coding__display": "General medical examination",
        "code__coding__system": "ICD 10",
        "code__coding__text": "General medical examination",
        "code__onset_datetime": "2014-10-01 00:00:00.0",
        "code__onset_duration": None,
        "code__onset_unit": None,
        "category__coding__0__code": "PRIMDIAG",
        "category__coding__0__display": "Principal",
        "category__coding__0__system": "BCONN",
        "category__text__0": "Principal",
        "category__coding__1__code": "diagnosis",
        "category__coding__1__display": "Diagnosis",
        "category__coding__1__system": "HL7",
        "category__text__1": "Diagnosis",
        "identifier__system": "BCONN",
        "identifier__type": "PatientProblemUID",
        "identifier__use": "official",
        "identifier__value": "13",
        "note__title": "Comment",
        "note__text": ""
    },
    {
        "severity": None,
        "body_site": "None",
        "asserted_date": "2014-10-01 13:20:35.55",
        "patient": "48-14-000019",
        "encounter": "O48-14-000010",
        "clinical_status": "active",
        "verification_status": "unknown",
        "asserter": "048140334",
        "code__coding__code": "I15.9",
        "code__coding__display": "Secondary hypertension, unspecified",
        "code__coding__system": "ICD 10",
        "code__coding__text": "Secondary hypertension, unspecified",
        "code__onset_datetime": "2014-10-01 00:00:00.0",
        "code__onset_duration": None,
        "code__onset_unit": None,
        "category__coding__0__code": "PRIMDIAG",
        "category__coding__0__display": "Principal",
        "category__coding__0__system": "BCONN",
        "category__text__0": "Principal",
        "category__coding__1__code": "diagnosis",
        "category__coding__1__display": "Diagnosis",
        "category__coding__1__system": "HL7",
        "category__text__1": "Diagnosis",
        "identifier__system": "BCONN",
        "identifier__type": "PatientProblemUID",
        "identifier__use": "official",
        "identifier__value": "16",
        "note__title": "Comment",
        "note__text": ""
    },
     {
        "severity": None,
        "body_site": "None",
        "asserted_date": "2014-10-01 13:20:35.55",
        "patient": "48-14-000019",
        "encounter": "O48-14-000010",
        "clinical_status": "active",
        "verification_status": "unknown",
        "asserter": "048140334",
        "code__coding__code": "I15.9",
        "code__coding__display": "Secondary hypertension, unspecified",
        "code__coding__system": "ICD 10",
        "code__coding__text": "Secondary hypertension, unspecified",
        "code__onset_datetime": "2014-10-01 00:00:00.0",
        "code__onset_duration": None,
        "code__onset_unit": None,
        "category__coding__0__code": "PRIMDIAG",
        "category__coding__0__display": "Principal",
        "category__coding__0__system": "trackcare",
        "category__text__0": "Principal",
        "category__coding__1__code": "diagnosis",
        "category__coding__1__display": "Diagnosis",
        "category__coding__1__system": "HL7",
        "category__text__1": "Diagnosis",
        "identifier__system": "BCONN",
        "identifier__type": "PatientProblemUID",
        "identifier__use": "official",
        "identifier__value": "16",
        "note__title": "Comment",
        "note__text": ""
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
result = get_raw_patient_json(data)
# print(json.dumps(result, indent=4, ensure_ascii=False))