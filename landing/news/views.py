from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import Newsform


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = { 'title': 'Главная' }
    # ^ Как вариант можно использовать, но джангой не рекомендуется
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True)
    

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'] ,is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'


class CreateNews(CreateView):
    form_class = Newsform
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    # ^^^^Для того что бы делать редирект на главную
    

# Функция для добавленя контента, аналог класса что выше^
# def add_news(request):
#     if request.method == 'POST':
#         form = Newsform(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(to=news)
#     else:
#         form = Newsform()
#     return render(request, 'news/add_news.html', {'form': form})