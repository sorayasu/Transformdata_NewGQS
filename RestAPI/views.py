# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import os, sys, django, json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from RestAPI.Tranformdata import get_raw_patient_json

import requests


class PatientTest(APIView):
    def post(self, request):
        raw = request.data
        query = raw['sql']
        config = raw['config']
        site = "his_" + raw['site']
        URL_API = "http://localhost:10011/new/"+site
        queryAPI = requests.post(URL_API,query)
        result = get_raw_patient_json(queryAPI.json(),config)
        return Response(result)

        
