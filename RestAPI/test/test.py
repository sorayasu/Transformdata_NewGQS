from flatten_json import unflatten_list
import json
from functools import reduce
import requests
from flatten_json import flatten, unflatten, unflatten_list


data = {'context': 'I02-17-000020', 'subject': '02-17-000023', 'status_system': 'TC', 'status_code': None, 'status_display': None, 'identifiers__system': 'TC', 'identifiers__type': 'OEORD_RowId', 'identifiers__use': 'official', 'identifiers__value': '9251829', 'contained__resource_type': 'Medication', 'contained__ingredient__coding__system': 'TC', 'contained__ingredient__coding__code': 1075, 'contained__ingredient__coding__display': 'Alcohol', 'contained__ingredient__text': 'Alcohol', 'contained__code__coding__system': 'TC', 'contained__code__coding__code': '51102707000059', 'contained__code__coding__display': 'Handi-C Hand Rub SOLUTION (240mL)', 'contained__code__text': 'Handi-C Hand Rub SOLUTION (240mL)', 'contained__from': None, 'contained__route__coding__system': 'BCONN', 'contained__route__coding__code': 'TOPI', 'contained__route__coding__display': 'Topical', 'contained__route__text': 'Topical', 'contained__method': None, 'contained__instruction_text': 'Handi-C Hand Rub SOLUTION (240mL)', 'contained__instruction_text_local': None, 'info_status_system': 'TC', 'info_status_code': 'V', 'info_status_display': 'Verified', 'patient_instruction': None, 'quantity': 1, 'dose_quantity': '1'}

def flatten_json(data):
    # print(unflatten_list(data, separator='__'))
    data = unflatten_list(data, separator='__')
    return data

# a = data.pop()
b = json.dumps(flatten_json(data))
print(b)