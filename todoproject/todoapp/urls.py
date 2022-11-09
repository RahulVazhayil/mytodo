
from django.urls import path, include

from . import views

app_name = 'todoapp'

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),


]