from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('ajouter/', ArticleCreateView.as_view(), name='article_create'),
    path('modifier/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('supprimer/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]