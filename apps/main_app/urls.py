
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^create$', views.create),
    url(r'^removefromlist/(?P<id>\d+$)', views.removefromlist),
    url(r'^addtolist/(?P<id>\d+$)', views.addtolist),
    url(r'^items/(?P<id>\d+)$', views.show),
]
