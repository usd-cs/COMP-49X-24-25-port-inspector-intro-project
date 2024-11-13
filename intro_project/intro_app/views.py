from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from . import forms

from .models import Post

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def view_posts(request):
    # get posts from database, and send them to render method
    posts = Post.objects.all().order_by("-created_at")
    comment_form = forms.CommentForm() #initialize the comment form
    return render(request, 'intro_app/homeNotSignedIn.html', {'posts': posts, 'form' : comment_form})

# This tag might be useful to limit creating a post for only users who are logged in
@login_required(login_url="/login/")
def new_post(request):
    # if the user is attempting to POST
    if request.method == "POST":
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            # if body is valid, save it
            newpost = form.save(commit=False)
            #save the author based on login of the request
            newpost.user = request.user
            newpost.save()
            #redirect the user back to homepage after post
            return redirect("/")
    #else it is a GET request, meaning the user is requesting the page, in which we should give them an empty form
    else: 
        form = forms.CreatePost()
    
    return render(request, 'createpost.html', { 'form' : form }) #passes in the form object we create above to our template, for rendering

@login_required(login_url="/login/")
def add_comment(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("/")
    else:
        form = forms.CommentForm()

    return render(request, 'intro_app/homeNotSignedIn.html', {'posts': posts, 'form' : form})


def login_view(request):
    # if recieveing a POST method, user is attempting to login
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # if user is properly authenticated
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/") # after the user logs in, send them to the homepage
    # if requesting the page, prompt form for authentication
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', { 'form' : form })

#log the user out and send them back to the homepage
def logout_view(request):
    logout(request)
    return redirect("/")