# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import os, sys, django, json
from RestAPI.models import Patient, Identifier, Name, Communication, Address, Contact, Organization
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from RestAPI.serializers import PatientSerializer, IdentifierSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from RestAPI.Tranformdata import get_raw_patient_json
from RestAPI.Transform_medication import get_raw_medication_json
from RestAPI.Transform_diagnosis import get_raw_diagnosis_json
import requests


class PatientTest(APIView):

    def get(self, request, type, val):
        posts1 = Identifier.objects.get(type=type, value=val).patient
        serializer = PatientSerializer(posts1, many=False)
        return Response(serializer.data)

    def post(self, request,type,val):
        # print(type,val)
        data = request.body
        site = "his_" + type
        URL_API = "http://localhost:10011/new/"+site
        queryAPI = requests.post(URL_API,data,headers={"content-type": "text/plain"}) #MIME
        if val == "medication":
            result = get_raw_medication_json(queryAPI.json())
        elif val == "diagnosis":
            result = get_raw_diagnosis_json(queryAPI.json())
        else: result = get_raw_patient_json(queryAPI.json())

        # serializer = PatientSerializer(data=data)
        # if serializer.is_valid():
        #     patient = serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     # patient = serializer.create(serializer.validated_data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(result)
        
