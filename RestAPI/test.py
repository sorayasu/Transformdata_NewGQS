from flatten_json import unflatten_list
import json
from functools import reduce
import requests
from flatten_json import flatten, unflatten, unflatten_list


data = [
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237712",
        "VitalSign__observation__value": "95.1",
        "VitalSign__observation__unit": "kg",
        "VitalSign__observation__value_range": None,
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "weight",
        "VitalSign__code__set_desc": "Weight",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237713",
        "VitalSign__observation__value": "173.5",
        "VitalSign__observation__unit": "Cms",
        "VitalSign__observation__value_range": None,
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "height",
        "VitalSign__code__set_desc": "Height",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237714",
        "VitalSign__observation__value": "31.59",
        "VitalSign__observation__unit": "Kg/m2",
        "VitalSign__observation__value_range": None,
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "bmi",
        "VitalSign__code__set_desc": "BMI",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237715",
        "VitalSign__observation__value": "2.09",
        "VitalSign__observation__unit": None,
        "VitalSign__observation__value_range": None,
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "bsa",
        "VitalSign__code__set_desc": "BSA",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237716",
        "VitalSign__observation__value": "36.5",
        "VitalSign__observation__unit": "* C",
        "VitalSign__observation__value_range": "36.5-37.5",
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "temperature",
        "VitalSign__code__set_desc": "Temperature",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237717",
        "VitalSign__observation__value": "96",
        "VitalSign__observation__unit": "/Min",
        "VitalSign__observation__value_range": "60-100",
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "pulse",
        "VitalSign__code__set_desc": "Pulse",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237718",
        "VitalSign__observation__value": "20",
        "VitalSign__observation__unit": "/Min",
        "VitalSign__observation__value_range": "17-22",
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "respiratory_rate",
        "VitalSign__code__set_desc": "Respiratory Rate",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237719",
        "VitalSign__observation__value": "130",
        "VitalSign__observation__unit": "mm Hg",
        "VitalSign__observation__value_range": "90-130",
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "systolic_bp",
        "VitalSign__code__set_desc": "Systolic BP",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    },
    {
        "VitalSign__observation__encounter": "O48-15-015283",
        "VitalSign__observation__patient": "48-14-000001",
        "VitalSign__observation__order_result_item_uid": "20141|237720",
        "VitalSign__observation__value": "82",
        "VitalSign__observation__unit": "mm Hg",
        "VitalSign__observation__value_range": "60-85",
        "VitalSign__observation__status": "final",
        "VitalSign__observation__issued": "2015-08-11 07:16:31.537",
        "VitalSign__observation__interpretation": None,
        "VitalSign__category__code": "vital-signs",
        "VitalSign__category__text": "Vital Signs",
        "VitalSign__code__setcode": "diastolic_bp",
        "VitalSign__code__set_desc": "Diastolic BP",
        "VitalSign__code__testcode": None,
        "VitalSign__code__test_desc": None
    }
]

def flatten_json(data):
    # print(unflatten_list(data, separator='__'))
    data = unflatten_list(data, separator='__')
    return data

a = data.pop()
b = json.dumps(flatten_json(a))
print(b)