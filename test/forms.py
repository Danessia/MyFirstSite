from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'test/post_list.html', {'posts': posts})

def choice_made(request):
    post_id = request.GET.get('post_id', None)
    chVal = ''
    if (post_id):
        post = Post.objects.get(id=int(post_id))
        if post is not None:
            post.chVar = post.var1
            chVal = post.chVar
            post.save()
    return HttpResponse(chVal)