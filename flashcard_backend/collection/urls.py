from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectionList.as_view()),
    path('<int:pk>/', views.CollectionDetail.as_view()),
]
