__author__ = 'techbk'

from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
from horizon import tabs
from openstack_dashboard.dashboards.techbk_head import api as log_api
#import json

class FirstTab(tabs.Tab):
    name = _("First Tab")
    slug = "first_tab"

    template_name = ("techbk_head/firstpanel/firsttab.html")  # noi de template minh dung
    preload = False
    def get_context_data(self, request, **kwargs):
        context = {}
        project = 'nova'
        context['json'] = log_api.projectlog(project)['test']
        #context['json'] = json.loads(log_api.projectlog(project))['test']
        print(context)
        return context


class SecondTab(tabs.Tab):
    name = _("Second Tab")
    slug = "second_tab"

    template_name = ("techbk_head/firstpanel/secondtab.html")  # noi de template minh dung
    preload = False

class FirstTabs(tabs.TabGroup):
    slug = "First_tabs"
    tabs = (FirstTab,SecondTab)
    sticky = True
