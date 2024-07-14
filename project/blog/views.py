from django.shortcuts import render
from django.http import HttpResponse
from .models import  Post

posts = [
    { 'title':'1','author': 'Author 1', 'content': 'Content 1'},
    { 'title':'2','author': 'Author 2', 'content': 'Content 2'},
    { 'title':'3','author': 'Author 3', 'content': 'Content 3'},
]

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html')