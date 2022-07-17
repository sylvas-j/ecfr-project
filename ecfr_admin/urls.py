from django.urls import path
from ecfr_admin import views

app_name = 'ecfr_admin'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    # path('find-result/', views.find_result_view, name='find_result'),
    path('change-password/', views.PasswordChangeView.as_view(), name='change_password'),
    path('search/table/', views.search_table, name='search_table'),
    path('logout', views.logoutUser, name='logout'),
]
