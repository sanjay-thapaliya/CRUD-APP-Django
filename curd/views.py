from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from curd.models import Blog


# Create your views here.


class LookBlog(ListView):
    model = Blog
    template_name = 'first.html'
    context_object_name = 'some'


class CreateBlog(CreateView):
    model = Blog
    template_name = 'Create.html'
    fields = ['first']
    success_url = reverse_lazy('see_blog')


class DeleteBLog(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('see_blog')


class UpdateBlog(UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ['first']
    success_url = reverse_lazy('see_blog')


