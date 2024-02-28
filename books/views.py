# REQUIREMENTS
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.db.models import F
from typing import Any
# MODELS
from books.models import Books



class IndexView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        
        context['books'] = Books.objects.all()
        context['title'] = 'Books Page'

        return context
    
    

class BookDetailView(DetailView):

    model = Books
    template_name = 'detailbook.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count = F('count') + 1)

        return context