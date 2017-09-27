from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cashflow$', views.cflist, name='cflist'),
    url(r'^cashflow/new$', views.showPMList, name='cfnew'),
    url(r'^cashflow/cfinput/(?P<pmId>\d+)/$', views.cfInput, name='cfinput'),
]