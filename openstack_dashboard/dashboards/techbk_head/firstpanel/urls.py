from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.techbk_head.firstpanel.views \
    import IndexView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
)
