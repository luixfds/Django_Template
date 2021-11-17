from django.views.generic import TemplateView

from home.models import Servicos, Equipe


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dados servicos'] = Servicos.objects.order_by('?').all()
        context['dados equipe'] = Equipe.objects.all()
        return context
