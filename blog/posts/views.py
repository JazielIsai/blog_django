from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import form
from .form import PublishForm
from .models import Publish


# Create your views here.
class HomePageView(ListView):
    model = Publish
    title = 'Inicio'
    template_name = 'posts/publish_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enable'] = False
        return context

    def get_queryset(self):
        return self.model.objects.filter(published=True).order_by('date_posted')


home_page_view = HomePageView.as_view()


class PostListView(LoginRequiredMixin, ListView):
    model = Publish
    title = 'Lista de Posts'
    template_name = 'posts/publish_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enable'] = True
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('date_posted')


post_list_view = PostListView.as_view()


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Publish
    title = 'Inicio'

    def get(self):
        post = self.get_object()
        post.published = True
        post.save()

        return redirect('posts:list_private')


post_detail_view = PostDetailView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Publish
    title = 'Crear'
    form_class = PublishForm
    template_name = 'posts/publish_form.html'
    success_url = reverse_lazy('posts:list_private')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print(form.instance.image)
        print('form.instance.image')
        form.instance.user = self.request.user
        return super().form_valid(form)


post_create_view = PostCreateView.as_view()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Publish
    title = 'Editar'
    template_name = 'posts/publish_form.html'
    form_class = PublishForm
    success_url = reverse_lazy('posts:list_private')


post_update_view = PostUpdateView.as_view()


class PostCompleteView(DetailView):
    model = Publish
    template_name = 'posts/publish_view.html'

    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs['key']
    #     data = self.model.objects.get(pk=pk)
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = data.title
    #     context['content'] = data.content
    #     context['image'] = data.image.url
    #     context['date_posted'] = data.date_posted
    #     context['published_date'] = data.published_date
    #     return context


post_complete_view = PostCompleteView.as_view()
