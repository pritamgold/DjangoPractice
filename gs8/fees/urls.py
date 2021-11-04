from django.urls import path
from . import views

urlpatterns = [
    path('fees1/', views.fees_one),
    path('fees2/', views.fees_two),
]