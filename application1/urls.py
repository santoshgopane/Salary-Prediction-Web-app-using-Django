from django.contrib import admin
from django.urls import path
from .import views
# from views import details

urlpatterns = [
    # path('', views.details,name='detail'),
    path('',views.linear,name='lin'),
    path('predict',views.predict,name='predict')
]