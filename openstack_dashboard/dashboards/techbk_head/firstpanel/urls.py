from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.techbk_head.firstpanel import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^list/$', views.list, name='list'),
)
