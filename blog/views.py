from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.models import UserProfile
from django.contrib import messages

from .models import BlogPost
from .forms import BlogForm


def post_list(request):
    if request.user.is_superuser:
        post_list = BlogPost.objects.filter().order_by('-post_created')
    else:
        post_list = BlogPost.objects.filter(status=1).order_by('-post_created')

    context = {
        'post_list': post_list,
        }

    return render(request, 'blog/blog.html', context)


def add_post(request):
    """adds new blog post"""
    form = BlogForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)