from django.shortcuts import render, get_object_or_404
from page.models import Post

# Create your views here.

# 홈 화면
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

# 디테일 화면
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})