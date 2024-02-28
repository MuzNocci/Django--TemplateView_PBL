from django.urls import path
from books import views



app_name = 'books'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),

]