from django.urls import path
from app2.views import *
app_name='somi'

urlpatterns=[
    path('pushpa/',pushpa,name='pushpa'),
    path('meghana/',meghana,name='meghana'),
]