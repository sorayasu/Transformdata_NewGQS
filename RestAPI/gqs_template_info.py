# import requests, json
# from functools import reduce

# class GQSTemplateInfo():
#     """
#         Generate SQL Statement from hmsservices.common.gqs_template
#     """
#     def __init__(self, models, *args, **kwargs):
#         self.raw_template_model = models
#         self.raw_models = models['template']
#         self.models = self._dict_to_array(models['template']) if self.raw_models else None
#         self.list_fields = self._listfields(self.models, 'source') if self.raw_models else []
#         self.gw_models = models['gw_models']

#         if 'config' in models:
#             self.template_config = models['config']
#         else:
#             self.template_config = None

#         self._query_utils = models.get('utils')
#         self.table = models['table']

#     def _dict_to_array(self, models):
#         if isinstance(models, dict):
#             return list(map(lambda x: {'key': x[0], 'source': self._dict_to_array(x[1])}, list(models.items())))
#         elif isinstance(models, list) and len(models) > 1:
#             result_list = []
#             for model in models:
#                 result_list = result_list + list(map(lambda x: {'key': x[0], 'source': self._dict_to_array(x[1])}, list(model.items())))
#             return result_list
#         elif isinstance(models, list):
#             return self._dict_to_array(models[0])
#         return models
    
#     def _append_list(self, x, y):
#         if isinstance(x, list):
#             if isinstance(y, list):
#                 return x + y
#             else:
#                 return x + [y]
#         else:
#             return [x] + [y]
        
#     def _listfields(self, data, key):
#         if isinstance(data, str):
#             return data
#         fields =  map(lambda x: self._listfields(x[key], key) , data)
#         return reduce(self._append_list, list(fields))
    
#     def get_raw_models(self):
#         return self.raw_models
    
#     def get_models(self):
#         return self.models
    
#     def get_list_fields(self):
#         return self.list_fields

#     def get_gw_models(self):
#         return self.gw_models

#     def get_template_config(self):
#         return self.template_config

#     def get_generate_sql_flag(self):
#         return self.raw_template_model['generate_sql'] if 'generate_sql' in self.raw_template_model else True
    
#     def get_raw_template_model_by_key(self, key):
#         try:
#             return self.raw_template_model[key]
#         except:
#             return None
        
#     def get_query_util(self, name):
#         try:
#             return self._query_utils[name]
#         except TypeError as e:
#             raise TypeError("query utils does not exist in this template.")
    
#     def generateSQL(self, params, **kwargs):
       
#         fields = ','.join(self.list_fields)
#         limit = "TOP {0}".format(kwargs.get('limit')) if kwargs.get('limit') and kwargs.get('limit') > -1 else ""
#         distinct = "DISTINCT" if kwargs.get('distinct') and isinstance(kwargs.get('distinct'), bool) else ""
#         return "SELECT {0} {1} {2} FROM {3}".format(limit, distinct, fields, self.table) if self.raw_models and self.get_generate_sql_flag() else self.table
