from django.urls import path
from . import views

app_name = 'courses_app'

urlpatterns = [
    path('', views.courses_view, name='courses_view'),
    path('no_permission/', views.no_permission_view, name='no_permission_view'),
]
