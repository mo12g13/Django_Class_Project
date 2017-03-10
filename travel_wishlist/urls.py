from django.conf.urls import  url
from . import views

urlpatterns =[
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited$', views.place_visited, name='place_visited'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
    url(r'^place/(?P<pk>\d+)', views.post_new_page, name='post_new_page')

]