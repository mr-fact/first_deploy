from django.urls import path
from .views import register_student, success_view

urlpatterns = [
    path('register/', register_student, name='register_student'),
    path('success/', success_view, name='success_url'),
]
