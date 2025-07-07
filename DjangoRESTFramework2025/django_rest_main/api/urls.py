from django.urls import path
from . import views






urlpatterns = [
    path('students/', views.studentsView),
    path('father/', views.fathersView),
    path('student/<int:pk>/', views.particularstudentView)
]