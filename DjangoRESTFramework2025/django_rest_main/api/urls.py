from django.urls import path
from . import views






urlpatterns = [
    path('students/', views.studentsView),
    path('father/', views.fathersView),
    path('student/<int:pk>/', views.particularstudentView),


    # BELOW IS A CLASS BASED VIEW EXAMPLE
    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>', views.ParticularEmployeeDetail.as_view()),


    # Below is for the Blogs Area
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('blogs/<int:pk>/', views.CommentDetailView.as_view())
]