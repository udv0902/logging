from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
import logging

logger = logging.getLogger(__name__)


class indexListView(ListView):
	logger.info('INFO')
	model = Post
	template_name = 'home.html'


class NewsDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


class NewsCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'content']


class NewsUpdateView(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'content']


class NewsDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')
