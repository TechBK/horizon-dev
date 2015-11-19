from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.techbk_head import dashboard

class Newpanel(horizon.Panel):
    name = _("New panel")
    slug = "newpanel"


dashboard.Techbk_Head.register(Newpanel)
