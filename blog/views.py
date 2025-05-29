from django.db.models.signals import post_save
from django.shortcuts import render
from .models import Post, kkexam
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').exclude(title__startswith='Первый')
    # post = Post.objects.get(id=1)
    # post.delete()

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def kkexam_list(request):
    exams = kkexam.objects.filter(is_public=True)
    return render(request, 'kkexam_list.html', {'exams': exams})