from django.urls import path
from . import views

urlpatterns = [
    path('', views.VidelList.as_view(), name='video')
]