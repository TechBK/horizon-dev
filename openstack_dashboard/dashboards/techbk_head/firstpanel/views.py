from horizon import views
from horizon import tabs

from openstack_dashboard.dashboards.mydashboard.mypanel \
    import tabs as my_tabs

class IndexView(tabs.TabView):
	tabs_group_class = my_tabs.FirstTabs
    # A very simple class-based view...
    template_name = 'techbk_head/firstpanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
