from django.urls import path
from . import views

urlpatterns = [
    path('form', views.form, name='form'),
    path('process_predict', views.prediction, name='process_predict'),
    path('information', views.information, name='information'),
    path('result', views.result, name='result'),
    path('download_file', views.download_file, name='download_file'),
    path('delete_data_user_input', views.delete_data_user_input, name='delete_data_user_input'),    
]