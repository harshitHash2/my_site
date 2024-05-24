from django.shortcuts import render
from .models import  Post

# Create your views here.

def starting_page(request):
    latest_post= Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_post,
    })

def posts(request) :
    all_p = Post.objects.all().order_by("-date")
    return render(request, "blog/allposts.html", {
        "all_p": all_p,
    })

def post_detail(request, slug) :
    one= Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {
        "post_d": one

    })