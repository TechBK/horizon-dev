__author__ = 'techbk'

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

class FirstTab(tabs.Tab):
    name = _("Instances Tab")
    slug = "first_tab"

    template_name = ("")#noi de template minh dung
    preload = False

    def get_instances_data(self):
    	#noi de code return context


class FirstTabs(tabs.TabGroup):
	slug = "First_tabs"
    tabs = (InstanceTab,)
    sticky = True