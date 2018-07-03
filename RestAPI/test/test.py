from flatten_json import unflatten_list
import json
from functools import reduce
import requests
from flatten_json import flatten, unflatten, unflatten_list


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
        "codes__code__coding__0__code": "Z00.0",
        "codes__code__coding__0__display": "General medical examination",
        "codes__code__coding__0__system": "ICD 10",
        "codes__code__text__0": "General medical examination",
        "codes__onset_datetime": "2014-10-01 00:00:00.0",
        "codes__onset_duration": None,
        "codes__onset_unit": None,
        "category__coding__0__code": "PRIMDIAG",
        "category__coding__0__display": "Principal",
        "category__coding__0__system": "BCONN",
        "category__text__0": "Principal",
        "identifier__system": "BCONN",
        "identifier__type": "PatientProblemUID",
        "identifier__use": "official",
        "identifier__value": "13",
        "note__title": "Comment",
        "note__text": "",
        "severity": None,
        "body_site": "None",
        "asserted_date": "2014-10-01 13:20:35.55",
        "patient": "48-14-000019",
        "encounter": "O48-14-000010",
        "clinical_status": "active",
        "verification_status": "unknown",
        "asserter": "048140334",
        "codes__code__coding__1__code": "I15.9",
        "codes__code__coding__1__display": "Secondary hypertension, unspecified",
        "codes__code__coding__1__system": "ICD 10",
        "codes__code__text__": "Secondary hypertension, unspecified",
        "codes__onset_datetime": "2014-10-01 00:00:00.0",
        "codes__onset_duration": None,
        "codes__onset_unit": None,
        "category__coding__1__code": "PRIMDIAG",
        "category__coding__1__display": "Principal",
        "category__coding__1__system": "BCONN",
        "category__text__1": "Principal",
        "identifier__system": "BCONN",
        "identifier__type": "PatientProblemUID",
        "identifier__use": "official",
        "identifier__value": "16",
        "note__title": "Comment",
        "note__text": "",
        "severity": None,
        "body_site": "None",
        "asserted_date": "2014-10-01 13:21:20.14",
        "patient": "48-14-000019",
        "encounter": "O48-14-000010",
        "clinical_status": "active",
        "verification_status": "unknown",
        "asserter": "048140334",
        "codes__code__coding__2__code": "F51.0",
        "codes__code__coding__2__display": "Nonorganic insomnia",
        "codes__code__coding__2__system": "ICD 10",
        "codes__code__text__": "Nonorganic insomnia",
        "codes__onset_datetime": "2014-10-01 00:00:00.0",
        "codes__onset_duration": None,
        "codes__onset_unit": None,
        "category__coding__2__code": "COMODIAG",
        "category__coding__2__display": "Comorbidity",
        "category__coding__2__system": "BCONN",
        "category__text__": "Comorbidity",
        "identifier__system": "BCONN",
        "identifier__type": "PatientProblemUID",
        "identifier__use": "official",
        "identifier__value": "19",
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

def join_row(prev, current):
    print("curr   ",current.items())
    dataobject = filter(lambda item: isinstance(item[1], list), current.items())
    # print("list   ", list(dataobject))
    # return reduce(union, dataobject, prev)

def flatten_json(data):
    # print(unflatten_list(data, separator='__'))
    data = unflatten_list(data, separator='__')
    print(json.dumps(data, indent=4, ensure_ascii=False))
    return data

result = get_raw_patient_json(data)
print(json.dumps(result, indent=4, ensure_ascii=False))