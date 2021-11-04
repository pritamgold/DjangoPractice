from django.urls import path
from . import views

urlpatterns=[
    path('course1/', views.cours_one),
    path('course2/', views.course_two),
]