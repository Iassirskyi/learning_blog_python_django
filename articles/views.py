from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionDenied
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from  django.contrib import messages

from .models import Article, Entry


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
    


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = Article
    fields = ('title',)
    template_name = 'article_update.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'New article was added')
        return super().form_valid(form)


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'



class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ('title', 'body',)
    template_name = 'entry_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'entry_delete.html'
    login_url = 'login'
    success_message = 'Entry was deleted'
    #success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(EntryDeleteView, self).delete(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('article_detail', kwargs ={'pk': self.object.article.id})


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entry_new.html'
    fields = ('title', 'body',)
    login_url = 'login'
    #success_url = reverse_lazy('article_list')


    def form_valid(self, form):
        form.instance.author = self.request.user
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        form.instance.article = article
        messages.success(self.request, 'New entry was added')
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('article_detail', kwargs ={'pk': self.object.article.id})
