import json
from functools import reduce
import requests
from flatten_json import unflatten_list
import RestAPI.transformutil as util

def get_raw_patient_json(query):
    transform_util = util.TransformUtil()
    try:
        # result = reduce(join_row, map(flatten_json, raw_data))
        result = reduce(transform_util.join_row, map(transform_util.flatten_json, query))
        # print(len(result))
    except Exception as e:
        print("error", e)
        result = {}
    return result
