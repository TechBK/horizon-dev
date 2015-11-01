__author__ = 'techbk'

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

class FirstTab(tabs.Tab):
    name = _("Instances Tab")
    slug = "instances_tab"

    template_name = ("")
    preload = False