from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('semester/<int:semester_id>/', views.semester, name = "semester"),
    path('subject/<int:subject_id>/', views.subject, name = "subject"),
]