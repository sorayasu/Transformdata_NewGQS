from functools import reduce
import RestAPI.transformutil as util


def get_raw_patient_json(query,config):
    transform_util = util.TransformUtil(config)
    result = reduce(transform_util.join_row, map(transform_util.flatten_json, query))
    if len(result) == 1:
        result = result.pop('data')
    return result