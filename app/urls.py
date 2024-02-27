from django.urls import path
from django.views.generic import TemplateView
from app import views



app_name = 'app'

urlpatterns = [

    path('', TemplateView.as_view(template_name='index.html', extra_context={'title':'Index Title', 'content':'Index body'}), name='index'),
    path('other/', views.OtherView.as_view(), name='other'),

]