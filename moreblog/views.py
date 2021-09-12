from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.generic import ListView, DetailView


#def blog(request):
    #return render(request, 'blog.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering =['-id']



class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'




