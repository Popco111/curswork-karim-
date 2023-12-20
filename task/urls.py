# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Другие URL-маршруты вашего приложения, если они есть

    path('', views.index, name='index'),  # Пример URL-маршрута для главной страницы
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
]
