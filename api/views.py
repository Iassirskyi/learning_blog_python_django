from rest_framework import generics

from articles.models import Article, Entry
from .serializers import ArticleSerializer, EntrySerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class EntryAPIView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
