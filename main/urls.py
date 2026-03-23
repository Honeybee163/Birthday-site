from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('memories/', views.memories, name='memories'),
    path('my-story/', views.story, name='story'),
    path('write-note/', views.write_note, name='write_note'),
    path('upload-memory/', views.upload_memory, name='upload_memory'),
]