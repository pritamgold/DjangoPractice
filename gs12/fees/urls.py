from django.urls import path
from . import views
urlpatterns = [
    path('learnfees/', views.fees_django)
]
