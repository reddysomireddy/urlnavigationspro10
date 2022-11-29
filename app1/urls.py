from django.urls import path
from app1.views import *
app_name='ganesh'

urlpatterns=[
    path('dj',dj,name='dj'),
]