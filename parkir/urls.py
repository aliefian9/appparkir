from django.urls import path

from . import views

urlpatterns = [
    path('', views.ParkirList.as_view()),
    path('<int:pk>/', views.ParkirDetail.as_view()),
]