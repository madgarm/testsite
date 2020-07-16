from django.urls import path

# email
# from django.conf.urls import url
# from . import views


from .views import *

urlpatterns = [
    path('', index),
    # email
    # path('sendemail', sendemail),
]