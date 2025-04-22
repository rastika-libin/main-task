from django.urls import path
from . import views

urlpatterns = [
    path('fill-form/', views.fill_form_redirect, name='fill_form'),
    path('form/', views.user_form, name='user_form'),
    path('admin-form/', views.admin_view, name='admin_form'),
    path('view-submissions/', views.view_submissions, name='view_submissions'),

]