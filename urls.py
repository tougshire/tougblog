from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy
from . import views

app_name = 'tougblog'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('tougblog:homepage'))),
    path('homepage/', views.HomePage.as_view(), name='homepage'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post'),
    path('page/<slug:slug>/', views.PageDetail.as_view(), name='page'),
    path('event/<slug:slug>/', views.EventDetail.as_view(), name='event')

]   
