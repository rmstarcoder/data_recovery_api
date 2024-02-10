from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('' ,FreetrilerView.as_view()),
    path('dashfree/' ,DashbrdFreetriler.as_view())
]