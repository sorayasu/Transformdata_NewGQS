from flatten_json import unflatten_list
import json
from functools import reduce

class TransformUtil:
    def __init__(self, config):
        self.config = config

    def flatten_json(self, data):
        data = self.addlist(unflatten_list(data, separator='__'))
        return data

    def addlist(self,data):
        for i, v in data.items():
            if type(v) is dict and i not in self.config['format_unlist']:
                self.addlist(v) 
                val = v
                data[i] = list()
                data[i].append(val)
            elif type(v) is dict and i in self.config['format_unlist']:
                self.addlist(v) 
                data[i] = dict()
                data[i].update(v)
            elif i in self.config['format_list_null']:
                data[i] = list()
        return data

    def union(self,fundamental, addkey):
        key, value = addkey
        if value[0] not in fundamental[key]:
            fundamental[key].append(value[0])
        return fundamental

    def join_row(self, prev, current):
        dataobject = filter(lambda item: isinstance(item[1], list), current.items())
        return reduce(self.union, dataobject, prev)

    # def groupping(self,data):
    #     try:
    #         # print('group', self.config['group']['check_med'])
    #         raw_json = [data[0]]
    #         raw_data = {}
    #         d = l ={}
    #         group_med = self.config['group']['group_unique_key']
    #         for i in range(len(data)-1):
    #             if data[i][self.config['group']['unique_key']] == data[i + 1][self.config['group']['unique_key']]:
    #                 raw_json.pop()
    #                 for k, v in data[i].items():
    #                     if data[i][k] == data[i + 1][k] and group_med not in k:
    #                         raw_data.update({k:v})
    #                     elif group_med in k :
    #                         grouping_data(raw_data, k, group_med, i)
    #                 raw_json.append(raw_data)
    #             else: 
    #                 raw_json.append(data[i+1])
    #         return raw_json
    #     except Exception as e:
    #         print("error", e)
    #         return data

    # def grouping_data(self,raw_data, key, group_med, index):
    #     keys = key.split(group_med)
    #     # set format index key
    #     _group = group_med
    #     _index = "__" + str(index)
    #     _key = keys[1]
    #     _value = data[index][key]
    #     format_dict(_group, _index, _key, _value)
    #     # add index key
    #     d = format_dict(_group, _index, _key, _value)
    #     _index = "__" + str(index + 1)
    #     _value = data[index + 1][key]
    #     l = format_dict(_group, _index, _key, _value)
    #     #update dict
    #     raw_data.update(d)
    #     raw_data.update(l)

    # def format_dict(_group, _index, _key, _value):
    #     # d = {"{}__{}{}".format(config['group_med'], i, x[1]:data[i][k])}
    #     return {_group + _index + _key : _value}