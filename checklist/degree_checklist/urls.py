from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("course_form/", views.course_form, name="course_form/"),
]