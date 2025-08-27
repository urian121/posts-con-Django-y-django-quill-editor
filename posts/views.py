from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})

def new_post(request):
    PostForm = modelform_factory(Post, fields=["title", "content"])
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "posts/new_post.html", {"form": form})
