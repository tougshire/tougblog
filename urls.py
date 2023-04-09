from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy
from . import views

app_name = 'tougblog'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('tougblog:homepage'))),
    path('homepage/', views.HomePage.as_view(), name='homepage'),
    path('post/<int:pk>/detail/', views.PostDetail.as_view(), name='post'),
    path('page/<slug:slug>/detail/', views.PageDetail.as_view(), name='page'),
    path('event/<int:pk>/detail/', views.EventDetail.as_view(), name='event')

]   
