from django.conf.urls import url
from .import views

urlpatterns = [
    url('', views.resumeFill, name='resume_fill'),
]
