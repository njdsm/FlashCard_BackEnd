from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlashcardList.as_view()),
    path('<int:pk>/', views.FlashcardDetail.as_view()),
]