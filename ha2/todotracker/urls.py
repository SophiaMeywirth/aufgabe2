from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:todo_id>/', views.edit, name='edit'),
    path('impressum/', views.impressum, name='impressum'),
]
