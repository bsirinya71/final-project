from django.urls import path
from . import views

urlpatterns = [
    #test upload model course
    path('upload', views.upload, name="upload"), 
    path('show', views.show, name="show"), 
    path('add_branch', views.add_branch, name="add_branch"), 
    path('show_branch', views.show_branch, name="show_branch"), 
    path('delete_branch/<str:id>', views.delete_branch, name="delete_branch"), 
    path('update_branch/<str:id>', views.update_branch, name="update_branch"), 
    
    
       
]