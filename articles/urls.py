from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleCreateListView.as_view(), name='articles'),
    path('<int:pk>/', views.ArticleRetrieveUpdateDeleteView.as_view()),
]
