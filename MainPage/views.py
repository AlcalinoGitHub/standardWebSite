from django.shortcuts import render, redirect
from django.http import HttpResponse
from social.models import Post, Comment
from django.contrib.auth.models import User, auth

def MainPage(request):
    Posts = list(Post.objects.all())
    Posts = Posts[::-1]
    Comentarios = list(Comment.objects.all())
    context = {
        'PostData': Posts,
        'Comentarios': Comentarios
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
        else:
            CurrentPost.LikedBy.remove(request.user.id)
            CurrentPost.Likes -= 1
            CurrentPost.save()
        print(CurrentPost.LikedBy)
        print(CurrentPost.Likes)

    return redirect('/')


def comment(request):
    if request.method == 'POST':
        data  = request.POST.get('comment')
        print(request.user)
        if data != '' and request.user.is_authenticated:
            PostID = request.POST.get('Post_id')
            CurrentPost = Post.objects.get(id = PostID)
            NewComment = Comment.objects.create(Content = data, Owner = request.user, PostedOn = CurrentPost)
            NewComment.save()
    return redirect('/')

def delete_comment(request):
    if request.method == 'POST':
        CommentId = request.POST.get('CommentID')
        CurrentComment = Comment.objects.get(id = CommentId)
        CurrentComment.delete()
    return redirect('/')
