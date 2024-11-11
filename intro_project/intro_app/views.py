from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from . import forms

from .models import Post

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def view_posts(request):
    # get posts from database, and send them to render method
    posts = Post.objects.all().order_by("-create_date")
    return render(request, 'home.html', {'posts': posts})

# This tag might be useful to limit creating a post for only users who are logged in
#@login_required(login_url="/users/login")
def new_post(request):
    # if the user is attempting to POST
    if request.method == "POST":
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            # if body is valid, save it
            newpost = form.save(commit=False)
            newpost.save()
            #redirect the user back to homepage after post
            return redirect("/")
    #else it is a GET request, meaning the user is requesting the page, in which we should give them an empty form
    else: 
        form = forms.CreatePost()
    
    return render(request, 'createpost.html', { 'form' : form }) #passes in the form object we create above to our template, for rendering