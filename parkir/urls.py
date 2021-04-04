from django.urls import path

from . import views

urlpatterns = [
    path('parkir/', views.ParkirList.as_view()),
    path('parkir/<int:pk>/', views.ParkirDetail.as_view()),
    path('jumlah/', views.JumlahList.as_view()),
    path('jumlah/<int:pk>/', views.JumlahDetail.as_view()),
]