from django.conf.urls import url, include
from django.http import HttpResponse
from RestAPI.views import PatientTest
from rest_framework.urlpatterns import *

urlpatterns = [
    # api
    url(r'^Query_api$', PatientTest.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)