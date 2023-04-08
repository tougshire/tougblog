from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy
from . import views

app_name = 'sdchomepage'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('sdchomepage:homepage'))),
    path('homepage/', views.HomePage.as_view(), name='homepage'),
    path('post/<int:pk>/detail/', views.PostDetail.as_view(), name='post'),
    path('page/<slug:slugw>/detail/', views.PostDetail.as_view(), name='page'),
    path('event/<int:pk>/detail/', views.EventDetail.as_view(), name='event')

]