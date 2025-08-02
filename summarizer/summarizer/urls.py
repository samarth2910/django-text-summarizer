from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # for GET /
    path('summarize/', views.summarize_text, name='summarize'),  # for POST /summarize/
]
