#!/usr/bin/env python
# coding=utf-8

"""
        Author  : Tinnarat Aromsuk
        Created : 20-Oct-2016
        Version : 0.1

        Updated by  : Thanut Pinsirodom
        Date        : 26-Oct-2016
        Version     : 0.2

        Updated by  : Tinnarat Aromsuk
        Date        : 05-Jan-2017
        Version     : 0.3

        Updated by  : Chailuck Chantaravisutlert 
        Date        : 25-May-2017
        Version     : 0.4
"""

import os
import json

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HMS_GATEWAY_SETTINGS_PATH = os.path.join(BASE_PATH, "settings.json")
HMS_GATEWAY_QUERIES_PATH = os.path.join(BASE_PATH, "queryservices", "queries.json")

class HMSConfigHelper():
    '''
        Use for get settings from file hms-gateway-settings.json
    '''
    def __init__(self, hms_settings_path = HMS_GATEWAY_SETTINGS_PATH, hms_queries_path = HMS_GATEWAY_QUERIES_PATH):
        if hasattr(self.__class__, 'instance'):
            raise Exception('cannot create intance (singleton).')
        self.__class__.instance = self
        try:
            with open(hms_settings_path, mode="r") as fp:
                self.settings_content = fp.read()
                fp.close()
                if len(self.settings_content) <= 0:
                    raise Exception("configuration file is empty.")
                else:  
                    try:
                      config = json.loads(self.settings_content)
                      self._hms_settings = config
                    except Exception as err:
                      raise err

            self._driver_lib_transform()
        except (IOError, Exception) as _error:
            raise _error

    def _driver_lib_transform(self):
        pass
        # if (self._hms_settings):
        #   data = self._hms_settings['adapter']['his']['driverlib']
        #   self._hms_settings['adapter']['his']['driverlib'] = eval(data)
        # else:
        #     raise Exception('Invalid HMS Setting')

    def get_config(self):
        '''
            Getting all settings in settings.json
        '''
        return self._hms_settings

    def load_from_url(self, url):
        '''
            Load settings from url
        '''
        import requests
        response = requests.get(url)
        self._hms_settings = response.json()

    def get_hms_settings(self, *args):
        '''
        :Example
          -get_hms_setting['hms-gateway.valet']['filewatcher']
        return {'commands': {'stop': 'http://localhost:5000/stop', 'start': 'http://localhost:5000/start'}
          -get_hms_setting('gqs','service.gqs')
         return
        :param key  is the service name:
        :return json setting of spacific service:
        '''
        temp = self._hms_settings
        for i in range(0, len(args)):
            temp = temp[args[i]]
        return temp

    def get_hms_setting_gqs(self):
        data=self._hms_settings['queries']
        return data

    def set_settings(self, settings):
        self._hms_settings = settings

    def is_hie(self):
        return "HIE" in self._hms_settings['settings']['organization']

    @staticmethod
    def get_instance():
        '''
            For get instance of singleton pattern
        '''
        if hasattr(HMSConfigHelper, 'instance'):
            return HMSConfigHelper.instance
        return HMSConfigHelper()

