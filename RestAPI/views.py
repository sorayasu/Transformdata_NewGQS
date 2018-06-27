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
import requests

headers =  {

       "Content-type": "application/json",
       "Accept": "text/plain"
    }


class PatientTest(APIView):

    def get(self, request, type, val):

        print(type, val)
        print(request.GET)
        # a = request.GET.get('identifier_type','None')
        # b = request.GET.get(r'value','None')

        posts1 = Identifier.objects.get(type=type, value=val).patient
        # posts1 = Patient.objects.filter(identifiers__type=type,identifiers__value=val)
        # print(posts1.name)
        print('..............')
        # serializer = IdentifierSerializer(posts1, many=True)
        serializer = PatientSerializer(posts1, many=False)
        return Response(serializer.data)

    def post(self, request):
        # print(request.body)
        data = request.body
        site = 'his_trakcare'
        URL_API = "http://localhost:10011/new/"+site
        queryAPI = requests.post(URL_API,data,headers={"content-type": "text/plain"}) #MIME
        # print(queryAPI.json())
        result = get_raw_patient_json(queryAPI.json())
        # print("*********",result)
        # serializer = PatientSerializer(data=data)
        # if serializer.is_valid():
        #     patient = serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     # patient = serializer.create(serializer.validated_data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(result)
        # return Response("True")
