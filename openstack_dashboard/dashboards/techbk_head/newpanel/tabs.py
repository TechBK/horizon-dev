__author__ = 'techbk'

from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
from horizon import tabs
from openstack_dashboard.dashboards.techbk_head import api as log_api

class NewTab(tabs.Tab):
    name = _("New Tab")
    slug = "new_tab"

    template_name = ("techbk_head/newpanel/newtab.html")  # noi de template minh dung
    preload = False

    def get_context_data(self, request, **kwargs):
        context = {}
        project = 'nova'
        context['log'] = log_api.projectlog(project)
        return context


class NewTabGroup(tabs.TabGroup):
    slug = "tabs_group"
    tabs = (NewTab,)
    sticky = True