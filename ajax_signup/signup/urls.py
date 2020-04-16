from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]
