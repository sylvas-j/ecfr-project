from django.urls import path
from subjects import views
from .views import (
    SubjectCreateView, SubjectListView, SubjectUpdateView, SubjectDeleteView,
    SubjectRegisteredCreateView, SubjectRegisteredListView, SubjectRegisteredUpdateView, SubjectRegisteredDeleteView
)

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
    path('create/', SubjectCreateView.as_view(), name='create_subject'),
    path('update/<int:pk>/', SubjectUpdateView.as_view(), name='update_subject'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='delete_subject'),

    # SubjectConbinations
    path('combination/create/', SubjectRegisteredCreateView.as_view(), name='create_subject_registered' ),
    path('registered/list/', SubjectRegisteredListView.as_view(), name='subject_registered_list' ),
    path('combination/update/<int:pk>', SubjectRegisteredUpdateView.as_view(), name='subject_registered_update' ),
    path('combination/delete/<int:pk>', SubjectRegisteredDeleteView.as_view(), name='subject_registered_delete' ),
    path('register/course/', views.subject_reg, name='subject_reg' ),
    path('registered/course/status/', views.subject_status, name='subject_status' ),
    

]