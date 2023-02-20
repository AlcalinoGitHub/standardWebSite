from django.shortcuts import render, redirect
from django.http import HttpResponse
from social.models import Post
from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404

def MainPage(request):
    Posts = list(Post.objects.all())
    Posts = Posts[::-1]
    context = {
        'PostData': Posts
    }


    if request.user.is_authenticated == False:
        return render(request, 'index.html', context)
    else:
        return render(request, 'UserLogged.html', context)
    
def LikePost(request):
    if request.method == 'POST' and request.user.is_authenticated:
        PostID = request.POST.get('Post_id')
        CurrentPost = Post.objects.get(id = PostID)
        if request.user.id not in CurrentPost.LikedBy:
            CurrentPost.LikedBy.append(request.user.id)
            CurrentPost.Likes += 1
            CurrentPost.save()
        print(CurrentPost.LikedBy)
        print(CurrentPost.Likes)

    return redirect('/')


def comment(request):
    if request.method == 'POST':
        Comment  = request.POST.get('comment')
        if Comment != '':
            PostID = request.POST.get('Post_id')
            CurrentPost = Post.objects.get(id = PostID)
            NewComment = {
                'author': str(request.user),
                'Content': Comment
            }
            CurrentPost.Comments.append(NewComment)
            CurrentPost.save()
            print(CurrentPost.Comments)
    return redirect('/')

def delete_comment(request):

    return redirect('/')
