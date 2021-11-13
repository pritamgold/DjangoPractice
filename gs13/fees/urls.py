from django.urls import path
from . import views

urlpatterns = [
    path('fees1/', views.Fees1),
    path('fees2/', views.Fees2),
]

