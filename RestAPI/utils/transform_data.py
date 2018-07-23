from functools import reduce
import RestAPI.utils.transform_util as util
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_raw_data_json(raw_json, config):
    if type(raw_json) == list and len(raw_json) < 1:
        result =  {"data":[]}
        logger.info(' empty result')
        return result
    transform_util = util.TransformUtil(config)
    result = reduce(transform_util.join_row, map(transform_util.flatten_json, raw_json))
    if len(result) > 1:
        logger.debug('add data to list')
        raw = dict()
        raw['data'] = [result]
        result = raw
    return result

