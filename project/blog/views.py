from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')  # List of posts

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # If you're using login
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'post_list.html', {'form': form, 'posts': posts})
