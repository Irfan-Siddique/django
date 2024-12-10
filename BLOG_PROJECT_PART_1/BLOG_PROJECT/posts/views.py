from django.shortcuts import render, redirect
from .forms import postForm
from .models import Post
# Create your views here.
def add_post(request):
    if request.method=='POST':
        addPostForm= postForm(request.POST)
        if addPostForm.is_valid():
            addPostForm.save()
            return redirect('add_post')
    else:
        addPostForm= postForm()
    return render(request,'add_post.html',{'form': addPostForm})


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    Post_Form= postForm(instance=post)
    print(post)
    if request.method=='POST':
        Post_Form= postForm(request.POST, instance=post)
        if Post_Form.is_valid():
            Post_Form.save()
            return redirect('homepage')

    return render(request,'add_post.html',{'form': Post_Form})


def delete_post(request, id):
    post= Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')