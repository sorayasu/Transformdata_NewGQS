import json
from functools import reduce
import requests
from flatten_json import unflatten_list
import RestAPI.transformutil as util

transform_util = util.TransformUtil()

def get_raw_diagnosis_json(query):
    try:
        result = reduce(transform_util.join_row, map(transform_util.flatten_json, query))
    except Exception as e:
        print("error", e)
        result = {}
    return result.get('data')

# result = get_raw_patient_json(data)
# print(json.dumps(result, indent=4, ensure_ascii=False))
# print(reduce(join_row, map(group_underscore_key, input_data)))