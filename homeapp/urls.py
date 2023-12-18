from django.urls import path
from . import views

urlpatterns = [

   # path('math/',views.addition,name="addition"),
    path('', views.demo, name='demo'),

]