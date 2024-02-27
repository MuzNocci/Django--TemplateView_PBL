# REQUIREMENTS
from django.views.generic import TemplateView
from typing import Any
# MODELS
from app.models import BaseTest



class OtherView(TemplateView):


    template_name = 'otherpage.html'


    def get_context_data(self, **kwargs) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        context['basetest'] = BaseTest.objects.get(id=1)
        context['title'] = 'Other Page (Database)'

        return context
