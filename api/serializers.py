from rest_framework import serializers

from articles.models import Article, Entry


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author',)


class EntrySerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    class Meta:
        model = Entry
        fields = ('id', 'title', 'body', 'author', 'article',)