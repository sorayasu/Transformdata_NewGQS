# -*- coding: utf-8 -*-
import os, sys, django, json
from rest_framework.response import Response
from rest_framework.views import APIView
from RestAPI.utils.Tranformdata import get_raw_data_json
import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

host = "localhost"
port = "10011"
context_path = "new"

class QueryService(APIView):
    def post(self, request):
        logger.debug('start paient post')
        raw = request.data
        logger.debug('raw data from POST : %s', raw)
        try:
            query = raw['sql']
            config = raw['config']
            site = raw['adapter']   
            url_api =   "http://{}:{}/{}/{}".format(host,port,context_path,site)
            logger.info('call to site %s',site)
            queryAPI = requests.post(url_api,query)
            logger.info('call to site %s',queryAPI)
            result = get_raw_data_json(queryAPI.json(),config)
            result.update({"message":"query success"})
            logger.info('result data : %s',result)
        except Exception as e:
            logger.debug(' Error to : %s', e)
            result =  {"data": [], "message":"query fail"} 
        return Response(result)  

        
