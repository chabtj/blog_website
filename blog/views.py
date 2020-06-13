from django.shortcuts import render
from .models import Post 
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
class BlogView(ListView):
	model=Post
	template_name='home.html'

class IndividualView(DetailView):
	model=Post
	template_name='individual.html'

class NewView(CreateView):
	model=Post
	template_name="add.html"
	fields="__all__"
	
class editview(UpdateView):
	model=Post
	template_name="edit.html"
	fields=['title','body']

class deleteview(DeleteView):
	model=Post
	template_name="delete.html"
	success_url= reverse_lazy('home')
