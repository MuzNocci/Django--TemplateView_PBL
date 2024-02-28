# REQUIREMENTS
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from django.db.models import F
from typing import Any
# MODELS
from app.models import BaseTest



class OtherView(TemplateView):

    template_name = 'otherpage.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        context['basetest'] = BaseTest.objects.get(id=1)
        context['title'] = 'Other Page Title'

        return context
    


class PostTaskView(RedirectView):

    pattern_name = 'app:singletask'

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:

       test = BaseTest.objects.filter(pk=kwargs['pk'])
       test.update(count = F('count') + 1)

       return super().get_redirect_url(*args, **kwargs)



class TaskView(TemplateView):

    template_name = 'otherpage3.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['test'] = get_object_or_404(BaseTest, pk=self.kwargs.get('pk'))
        context['title'] = 'Other Page Title (After Redirect)'

        return context