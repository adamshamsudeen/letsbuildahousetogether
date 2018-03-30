from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Home( TemplateView):
    # login_url = '/login/'
    # success_url = "/restaurants/"
    template_name = 'dream/index.html'
   


    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # search = self.request.GET.get('q')
        # rows_to_search = ('user_id', 'os', 'browser','country','device_type','ip')
        
        # Q_filter = reduce(lambda x, y: x | Q(**{"{}__iregex".format(y): search}), rows_to_search, Q())
        # if search:
        #     if VisitorInfo.objects.filter(Q_filter).filter(active=True).count() >0:
        #         context['list_no'] = VisitorInfo.objects.filter(Q_filter).filter(active=True)
        #     else:
        #         context['list_no'] = "N"
        # else:
        #     context['list_no'] = VisitorInfo.objects.filter(active=True).order_by('last_active')
        # context['persona_list'] = Persona.objects.all()
        return context
