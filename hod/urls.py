from django.urls import path
from hod import views

# from hod.views import (
#     HodDeleteView
# )


app_name = 'hod'

urlpatterns = [
    path('list/', views.hod_list, name='hod_list'),
    path('create/', views.hod_create, name='hod_create'),
    path('update/<int:pk>', views.hod_detail, name='hod_update'),
    path('details/edit/', views.hod_edit, name='hod_edit'),
    # path('courses/', views.hod_courses, name='hod_courses'),
    path('courses/list/', views.hod, name='hod'),
    # path('courses/list/<int:pk>', views.hod_courses_list, name='hod_courses_list'),
    # path('courses/delete/<int:pk>', views.delete_course, name='delete_course'),
]