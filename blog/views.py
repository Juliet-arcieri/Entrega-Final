from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm

def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def about(request):
    return render(request, 'blog/about.html')

def home(request):
    return render(request, 'blog/home.html')

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog.html', {'form': form})
