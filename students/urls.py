from django.urls import path

from students import views
from students.views import (
    DashboardView, StudentCreateView, StudentListView, StudentUpdateView, StudentDeleteView
)


app_name = 'students'

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    # path('', StudentListView.as_view(), name='student_list'),
    path('', views.StudentList.student_list, name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    
    # path('list/', views.result_list, name='result_list'),
    # path('courses/list/', views.subject_list, name='subject_list'),
    # path('display/', views.result_display, name='result_display'),
    path('details/edit', views.student_edit, name='student_edit'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete'),
]
