from django.conf.urls import url, include
from django.http import HttpResponse
from RestAPI.views.views import QueryService
from rest_framework.urlpatterns import *

urlpatterns = [
    # api
    url(r'^query$', QueryService.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)