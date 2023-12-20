from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('jipdv', views.index, name='main'),
    path('about-us', views.about, name='about'),
    path('index/id:task_id',index,name='index')
   ]