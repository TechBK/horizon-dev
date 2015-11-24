from django.utils.translation import ugettext_lazy as _

import horizon

class LogPanels(horizon.PanelGroup):
    slug = "logpanels"
    name = _("LogPanels")
    panels = ('overview','detail')

class LogDashboard(horizon.Dashboard):
    name = _("LogDashboard")
    slug = "logdashboard"
    panels = (LogPanels,)  # Add your panels here.
    default_panel = 'overview'  # Specify the slug of the dashboard's default panel.
    permissions = ('openstack.roles.admin',)


horizon.register(LogDashboard)
