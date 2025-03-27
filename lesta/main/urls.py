from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('file/<int:id>/', views.results, name='results')
]