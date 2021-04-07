from django.urls import path

from .views import (ArticleListView, 
                    ArticleDetailView, 
                    ArticleUpdateView, 
                    EntryUpdateView, 
                    EntryDeleteView, 
                    ArticleDeleteView, 
                    ArticleCreateView, 
                    EntryCreateView,
                    EntryDetailView)


urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/new_entry/', EntryCreateView.as_view(), name='entry_new'),
    path('entry_detail/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('<int:pk>/edit_entry/', EntryUpdateView.as_view(), name='entry_edit'),
    path('<int:pk>/edit_entry/delete/', EntryDeleteView.as_view(), name='entry_delete'),
]