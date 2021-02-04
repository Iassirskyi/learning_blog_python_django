from django.urls import path

from .views import ArticleAPIView, ArticleDetailAPIView, EntryAPIView, EntryDetailAPIView


urlpatterns = [
    path('v1/articles/', ArticleAPIView.as_view(), name='articles'),
    path('v1/articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('v1/entries/', EntryAPIView.as_view(), name='entries'),
    path('v1/entries/<int:pk>/', EntryDetailAPIView.as_view(), name='entry_detail'),
]