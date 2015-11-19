from horizon import views
from horizon import tabs

from openstack_dashboard.dashboards.techbk_head.firstpanel \
    import tabs as my_tabs

class IndexView(tabs.TabView):
    tab_group_class = my_tabs.FirstTabs
    # A very simple class-based view...
    template_name = 'techbk_head/firstpanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context






















"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from openstack_dashboard.dashboards.techbk_head.firstpanel.models import Document
#from myproject.myapp.models import Document
from openstack_dashboard.dashboards.techbk_head.firstpanel.forms import DocumentForm
#from myproject.myapp.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'])
            #newdoc = Document(docfile = request.FILES['docfile'])
            #newdoc.save()

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            return HttpResponseRedirect('/techbk_head/list')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    #documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'techbk_head/firstpanel/uploadfile.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def handle_uploaded_file(f):

    filename = 'openstack_dashboard/dashboards/techbk_head/firstpanel/pcap/'+ f.name
    #filename = 'pcap/'+ f.name
    destination = open(filename, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()"""