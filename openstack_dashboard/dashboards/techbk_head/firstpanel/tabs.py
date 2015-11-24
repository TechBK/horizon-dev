__author__ = 'techbk'

from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
from horizon import tabs


class FirstTab(tabs.Tab):
    name = _("First Tab")
    slug = "first_tab"

    template_name = ("techbk_head/firstpanel/firsttab.html")  # noi de template minh dung
    preload = False

    def get_instances_data(self):
        pass
        # noi de code return context

class SecondTab(tabs.Tab):
    name = _("Second Tab")
    slug = "second_tab"

    template_name = ("techbk_head/firstpanel/secondtab.html")  # noi de template minh dung
    preload = False

    def get_instances_data(self):
        pass
        # noi de code return context

class FirstTabs(tabs.TabGroup):
    slug = "First_tabs"
    tabs = (FirstTab,SecondTab)
    sticky = True
