from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.interaction, name='new_interaction'),
    path('triangle_coloring', views.triangle, name='triangle_coloring'),
    path('home_page', views.home, name='home_page'),
    path('cover', views.cover, name='cover')
]

