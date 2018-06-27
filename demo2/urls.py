"""demo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from django.http import HttpResponse
# from rest_framework import routers
from RestAPI.views import PatientTest
from rest_framework.urlpatterns import *

# router = routers.DefaultRouter()
# router.register(r'Patient', views.PatientViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    # api
    url(r'^Patient/(?P<type>[A-Z]+)/(?P<val>[0-9a-z\-]+)$', PatientTest.as_view()),
    url(r'^Query_api$', PatientTest.as_view())
    # url(r'^Patient/(?P<name>[a-z]+),(?P<active>[a-z]+),(?P<telecom>[a-z]+),(?P<gender>[a-z]+),(?P<active>[a-z]+)', PatientTest.as_view()),
    # url(r'^api/v1/posts/(?P<pk>[0-9]+)$', 'post_element')
]
urlpatterns = format_suffix_patterns(urlpatterns)