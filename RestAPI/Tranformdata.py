import json
from functools import reduce
import requests
from flatten_json import unflatten_list
import RestAPI.transformutil as util
import logging


def get_raw_patient_json(query,config):
    transform_util = util.TransformUtil(config)
    result = reduce(transform_util.join_row, map(transform_util.flatten_json, query))
    if len(result) == 1:
        result = result.pop('data')
    return result