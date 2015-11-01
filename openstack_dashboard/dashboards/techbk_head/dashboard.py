from django.utils.translation import ugettext_lazy as _

import horizon


class Mygroup(horizon.PanelGroup):
    slug = "firstgroup"
    name = _("First Group")
    panels = ('firstpanel',)

class Techbk_Head(horizon.Dashboard):
    name = _("Techbk Head")
    slug = "techbk_head"
    panels = (Mygroup,)  # Add your panels here.
    default_panel = 'firstpanel'  # Specify the slug of the dashboard's default panel.


horizon.register(Techbk_Head)
