# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db import models
from RestAPI import models as patient_models

class NameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patient_models.Name
        fields = ('prefix', 'given_name', 'middle_name', 'family_name','suffix','language')

class CommunicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patient_models.Communication
        fields = ('language', 'preferred')

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patient_models.Address
        fields = ('line', 'city', 'district', 'state','country','postcode')

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patient_models.Contact
        fields = ('system', 'use', 'value')

class OrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = patient_models.Organization
        fields = ('code_name', 'code_number', 'name')

class IdentifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = patient_models.Identifier
        fields = ('type', 'value', 'facility', 'start', 'end')


class PatientSerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer(many=True, required=True, source="identifiers")
    name = NameSerializer(many=True, required=True, source="names")
    communication = CommunicationSerializer(many=True, required=True, source="communications")
    address = AddressSerializer(many=True, source='addresss')
    contact = ContactSerializer(many=True, required=True, source="contacts")
    organization = OrganizationSerializer(many=False, required=True)
    

    class Meta:
        model = patient_models.Patient
        fields = ('resource_type', 'row_id', 'identifier', 'name','gender','birth_date','nationality','religion','communication','address','deceased','deceased_datetime','marital_status','contact','organization')

    def create(self, validated_data):
        print("create work")
        
        ou = validated_data.pop('organization')

        # #add value organziation use "get_or_create" when duplicate data in a table to have one id
        org = patient_models.Organization.objects.get_or_create(**ou)[0]

        # pop data in list for add value of patient
        identifier_data = validated_data.pop('identifiers')
        name_data = validated_data.pop('names')
        communication_data = validated_data.pop('communications')
        address_data = validated_data.pop('addresss')
        contact_data = validated_data.pop('contacts')
        # print(validated_data)

        patient = patient_models.Patient.objects.create(organization=org,**validated_data)

        # loop add data each table
        for x in identifier_data:
            patient_models.Identifier.objects.get_or_create(patient=patient,**x)
        # patient_models.Identifier.objects.create(**identifier_data)
        for x in name_data:
            patient_models.Name.objects.create(patient=patient,**x)

        for x in communication_data:
            patient_models.Communication.objects.create(patient=patient,**x)

        for x in address_data:
            patient_models.Address.objects.create(patient=patient,**x)

        for x in contact_data:
            patient_models.Contact.objects.create(patient=patient,**x)

        return patient
