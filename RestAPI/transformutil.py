from flatten_json import unflatten_list
import json
from functools import reduce

formatt_list = ['code','route','text','organization']
format_list_null = ['note']

class TransformUtil:
    # def __init__(self):
    #     pass
    
    def flatten_json(self, data):
        data = self.addlist(unflatten_list(data, separator='__'))
        return data

    def addlist(self,data):
        # print("2   ", data)
        for i, v in data.items():
            if type(v) is dict and i not in formatt_list:
                # print("v   ",i ,    v)
                self.addlist(v) 
                val = v
                data[i] = list()
                data[i].append(val)
            elif type(v) is dict and i in formatt_list:
                    self.addlist(v) 
                    data[i] = dict()
                    data[i].update(v)
        return data

    def union(self,fundamental, addkey):
        key, value = addkey
        if value[0] not in fundamental[key]:
            fundamental[key].append(value[0])
        return fundamental

    def join_row(self, prev, current):
        dataobject = filter(lambda item: isinstance(item[1], list), current.items())
        return reduce(self.union, dataobject, prev)