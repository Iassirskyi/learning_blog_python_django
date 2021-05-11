from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)


    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Entry(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=255)
    body = models.TextField()
    screen = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = 'Entries'

    def __str__(self):
        if len(self.body) > 50:
            return f'{self.body[:50]}...'
        else:
            return self.body

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.article.id})
