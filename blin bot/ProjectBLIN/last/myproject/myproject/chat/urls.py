from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-message/', views.send_message, name='send_message'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('record-voice/', views.record_voice, name='record_voice'),
]
