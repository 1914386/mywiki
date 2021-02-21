from django.shortcuts import render, get_object_or_404, redirect
from page.models import Post, Comment
from django.utils import timezone
from .forms import postUpdate

# Create your views here.

# 홈 화면
def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'home.html', {'posts':posts, 'comments':comments})

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

# 글 수정 함수
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = postUpdate(request)
        post.title = request.POST['title']
        post.text = request.POST['text']
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.update_date = timezone.now()
        post.save()
        return redirect('/post/' + str(post.id))
    
    else:
        form = postUpdate(instance=post)
        return render(request, 'update.html', {'form':form})

# 글 삭제 함수
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

# 댓글 화면
def comment(request):
    return render(request, 'comment.html')

# 댓글 저장 함수
def comment_write(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment = Comment()
    if request.method == 'POST':
        comment.create_date = timezone.now()
        comment.content = request.POST['content']
        comment.save()
        return render(request, 'home.html', {'posts':posts, 'comments':comments})