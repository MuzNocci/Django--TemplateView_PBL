from django.urls import path
from django.views.generic import TemplateView, RedirectView
from app import views



app_name = 'app'

urlpatterns = [

    path('', TemplateView.as_view(
        template_name='index.html', 
        extra_context={'title':'Index Title', 'content':'Index body'}),
        name='index'),

    path('other/', views.OtherView.as_view(), name='other'),

    path('redirect/', RedirectView.as_view(url='https://muller.nocciolli.com.br/'), name='go-to-muller'),

    path('other2/<int:pk>', views.PostTaskView.as_view(), name='posttask'),

    path('other3/<int:pk>', views.TaskView.as_view(), name='singletask'),

]