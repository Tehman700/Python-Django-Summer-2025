from django.urls import path
from . import views






urlpatterns = [
    path('students/', views.studentsView),
    path('father/', views.fathersView),
    path('student/<int:pk>/', views.particularstudentView),


    # BELOW IS A CLASS BASED VIEW EXAMPLE
    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>', views.ParticularEmployeeDetail.as_view())
]