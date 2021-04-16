from django.urls import path
from . import views

app_name = 'recruit'
urlpatterns = [
    path('list/', views.list_announcement),
]
