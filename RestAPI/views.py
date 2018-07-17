# -*- coding: utf-8 -*-
import os, sys, django, json
from rest_framework.response import Response
from rest_framework.views import APIView
from RestAPI.Tranformdata import get_raw_patient_json
import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class PatientTest(APIView):
    def post(self, request):
        raw = request.data
        try:
            query = raw['sql']
            config = raw['config']
            site = raw['adapter']   
            URL_API = "http://localhost:10011/new/"+site
            queryAPI = requests.post(URL_API,query)
            result = get_raw_patient_json(queryAPI.json(),config)
            return Response(result)
        except Exception as e:
            logger.debug('Error to : %s', e)
            result =  {} 
            return Response(result)  

        
