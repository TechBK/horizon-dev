from horizon import views


class IndexView(views.APIView):
	tab_group_class = mydashboard_tabs.MypanelTabs
    # A very simple class-based view...
    template_name = 'mydashboard/mypanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
