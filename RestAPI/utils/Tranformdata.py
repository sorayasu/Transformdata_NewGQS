from functools import reduce
import RestAPI.utils.transformutil as util
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_raw_data_json(query,config):
    transform_util = util.TransformUtil(config)
    result = reduce(transform_util.join_row, map(transform_util.flatten_json, query))
    if len(result) > 1:
        logger.debug('add data to list')
        raw = {}
        raw['data'] = [result]
        result = raw
    return result

