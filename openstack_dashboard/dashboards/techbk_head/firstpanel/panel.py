from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.techbk_head import dashboard

class Firstpanel(horizon.Panel):
    name = _("First Panel")
    slug = "firstpanel"


dashboard.Techbk_Head.register(Firstpanel)
