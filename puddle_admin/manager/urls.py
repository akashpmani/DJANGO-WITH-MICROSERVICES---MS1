from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name ='test'),
    path('t',views.home1,name ='test1')
]