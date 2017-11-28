from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm, PostForm, PostEditForm


class PostList(ListView):
	model = Post
    #template_name = 'korea/board.html'
    #paginate_by = 9
    #queryset = Post.objects.all()


class PostDetail(DetailView):
    model = Post
    template_name = 'korea/post_detail.html'


class KoreaBoard(ListView):
    template_name = 'korea/board.html'
    model = Post


class PostAdd(FormView):
    model = Post
    template_name = 'korea/post_add.html'
    form_class = PostForm
    fields = ['title', 'country','content','image']
    success_url = reverse_lazy('korea')

    def form_valid(self, form):
        post = Post()
        form.instance.user = self.request.user

        post = form.save()
        return super(PostAdd, self).form_valid(form)


class PostEdit(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'korea/post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'korea/post_delete.html'
    success_url = reverse_lazy('korea')


