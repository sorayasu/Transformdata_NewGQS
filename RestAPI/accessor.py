import requests
# from hmsexceptions import HISDataNotFound, AdapterError
from gqs_template_info import GQSTemplateInfo
from confighelper import HMSConfigHelper

confighelper = HMSConfigHelper.get_instance()
adapter_port = confighelper.get_hms_settings('microservices', 'adapter', 'port')


class Accessor():
    """
        Base class for retrieve data from HIS.
    """
    def __init__(self, template, *args, **kwargs):

        self.params = args
        self.template = template
        self.gqs_template_info = GQSTemplateInfo(self.template)
        self.statement = self.get_statement(**kwargs)

    def get_statement(self, **kwargs):
        if not hasattr(self, 'statement'):
            self.statement = self.gqs_template_info.generateSQL(self.params, **kwargs)
        return self.statement

    def get_gqs_template_info(self):
        return self.gqs_template_info

    def get_template(self):
        return self.template

    def retrieve_utils(self, name, params):
        statement = self.get_gqs_template_info().get_query_util(name)
        try:
            adapter = self.template['adapter']
            r = requests.post("http://localhost:{0}/{1}".format(adapter_port, adapter), data=statement.format(*params), headers={"content-type": "text/plain"}, timeout=60)
            result = r.json()
            if ('ERROR' in result and len(result) == 1):
                raise AdapterError(result['ERROR'])
            if not result:
                raise HISDataNotFound(f"adapter_port:{adapter_port} adapter:{adapter} params:{params}")
            return result
        except Exception as e:
            raise e

    def retrieve(self):
        try:
            adapter = self.template['adapter']
            r = requests.post("http://localhost:{0}/{1}".format(adapter_port, adapter), data=self.statement.format(*self.params), headers={"content-type": "text/plain"}, timeout=60)
            result = r.json()
            result = self.clean_data_result(result)
            if ('ERROR' in result and len(result) == 1):
                raise AdapterError(result['ERROR'])
            if not result:
                raise HISDataNotFound(f"adapter_port:{adapter_port} adapter:{adapter} params:{self.params}")
            return result
        except Exception as e:
            raise e

    def get_params_from_utils(self):
        utils_as_params = self.gqs_template_info.get_raw_template_model_by_key('utils_as_params')
        if utils_as_params:
            data_list = self.retrieve_utils(utils_as_params['utils'], self.params)
            
            if utils_as_params['params_type'] == 'string':
                if data_list and len(data_list[0]) == 2:
                    separator = utils_as_params["params_separator"]
                    result = ['', '']
                    for data in data_list:
                        if data[0] and data[1]:
                            result[0] = result[0] + str(data[0])
                            result[1] = result[1] + str(data[1])
                            if separator:
                                result[0] = result[0] + separator
                                result[1] = result[1] + separator
                    if separator:         
                        result[0] = result[0][:-1]
                        result[1] = result[1][:-1]
                    return result
        else:
            return self.params

    def clean_data_result(self, raw_data):
        clean_result = self.gqs_template_info.get_raw_template_model_by_key('clean_result')
        if clean_result and (raw_data and ('cause' not in raw_data and len(raw_data) != 1)):
            valid_data_pos = clean_result['valid_data_pos']
            _raw_data = list()
            for data in raw_data:
                is_valid = True
                for pos in valid_data_pos:
                    if not data[pos]:
                        is_valid = False
                        break
                if is_valid:
                    _raw_data.append(data)
            return _raw_data
        else:
            return raw_data