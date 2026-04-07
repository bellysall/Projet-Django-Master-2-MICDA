from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    ordering = ['-date_publication']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')