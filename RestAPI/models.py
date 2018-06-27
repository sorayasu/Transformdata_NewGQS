from django.db import models
# -*- coding: utf-8 -*-

# Create your models here.

class Organization(models.Model):
    code_name = models.CharField(max_length=20)
    code_number = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'organization'
    
    # def __str__(self):
    #     return self.name

class Patient(models.Model):
    row_id = models.CharField(max_length=100, null=True, default=None, unique=True)
    resource_type = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    deceased = models.BooleanField(default=False)
    deceased_datetime = models.DateTimeField(null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=100, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name='patient_org', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'patient'

class Identifier(models.Model):
    patient = models.ForeignKey(Patient, related_name='identifiers', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    facility = models.CharField(max_length=100)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'Identifier'

class Name(models.Model):
    patient = models.ForeignKey(Patient, related_name='names', on_delete=models.CASCADE)
    prefix = models.CharField(max_length=100, blank=True, null=True)
    given_name = models.CharField(max_length=100, db_index=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    family_name = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    suffix = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'Name'

class Communication(models.Model):
    patient = models.ForeignKey(Patient, related_name='communications', on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    preferred = models.BooleanField(default=False)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'Communication'

class Address(models.Model):
    patient = models.ForeignKey(Patient, related_name='addresss', on_delete=models.CASCADE)
    line = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'Address'

class Contact(models.Model):
    patient = models.ForeignKey(Patient, related_name='contacts', on_delete=models.CASCADE)
    system = models.CharField(max_length=100)
    use = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100)

    class Meta:
        app_label = 'RestAPI'
        db_table = 'Contact'
