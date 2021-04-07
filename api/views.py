from rest_framework import generics, permissions

from articles.models import Article, Entry
from .serializers import ArticleSerializer, EntrySerializer
from .permissions import IsAuthorReadOnly


class ArticleCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorReadOnly,)
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorReadOnly,)
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class EntryAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorReadOnly,)
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorReadOnly,)
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
