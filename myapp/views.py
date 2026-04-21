from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


def index(request):
    """Home page view"""
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'myapp/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'myapp/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'myapp/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'myapp/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
