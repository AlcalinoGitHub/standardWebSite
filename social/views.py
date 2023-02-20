from django.shortcuts import render, redirect
from django.http import HttpResponse
from social.models import Post
from django.contrib import messages
# Create your views here.

def Posts(request):
    if request.method == 'POST':
        Title = request.POST['title']
        Content = request.POST['content']
        if Title != '' and Content != '':
            NewPost = Post.objects.create(Title = Title, Content = Content, Owner = request.user)
            NewPost.save()
            messages.info(request, 'Published!')
            return redirect('/posts/')
        else:
            messages.info(request, 'Fields cant be empty')
            return redirect('/posts/')
    else:
        UserPosts = Post.objects.filter(Owner = request.user)
        context = {
            'Publicaciones': UserPosts
        }
        return render(request, 'Posts.html', context)
    
def delete(request):
    if request.method == 'POST':
        PostId = request.POST.get('post_id')
        CurrentPost = Post.objects.get(id = PostId)
        CurrentPost.delete()
        print(PostId)

    return redirect('/posts/')
    