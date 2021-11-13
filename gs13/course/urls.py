from django.urls import path
from . import views

urlpatterns = [
    path('course1/', views.Course1),
    path('course2/', views.Course2),
]

