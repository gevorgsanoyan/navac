from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stock$', views.stocklist, name='stlist'),
    url(r'^stock/new$', views.stocknew, name='stnew'),
    url(r'^stock/edit/(?P<sId>\d+)/$', views.stockedit, name='stedit'),
    url(r'^stock/spflist/(?P<sId>\d+)/$', views.stockPFList, name='spflist'),
    url(r'^stock/spfinput/(?P<sId>\d+)/$', views.stockPFDatesInput, name='spfinput'),
    url(r'^stock/spfedit/(?P<spfId>\d+)/$', views.stockPFDatesEdit, name='spfedit'),
]