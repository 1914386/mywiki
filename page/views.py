from django.shortcuts import render, get_object_or_404, redirect
from page.models import Post
from django.utils import timezone

# Create your views here.

# 홈 화면
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

# 디테일 화면
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

# 새 글 작성 화면
def create(request):
    return render(request, 'create.html')

# 글 저장 함수
def postcreate(request):
    post = Post()
    post.title = request.POST['title']
    post.text = request.POST['text']
    if 'image' in request.FILES:
        post.image = request.FILES['image']
    post.update_date = timezone.now()
    post.save()
    return redirect('/post/' + str(post.id))