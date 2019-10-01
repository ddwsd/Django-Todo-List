from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addItem, name='add'),
    path('toggleComplete/<list_id>', views.toggleComplete, name='complete'),
    path('delete', views.deleteItem, name='delete'),
]
