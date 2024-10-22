from dataclasses import fields
from datetime import datetime

from django.forms import modelformset_factory
from django.http import HttpResponse
from forumApp.posts.forms import PostBaseForm

from django.shortcuts import render, redirect
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm
from forumApp.posts.models import Post


def index(request):
    post_form = modelformset_factory(
        Post,
        fields=('title', 'content', 'author', 'languages'),
        error_messages={
            'title': "Title is required!",
        }
    )

    context = {
        "my_form": post_form(request.POST),
    }

    return render(request, 'common/index.html', context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect('dash')
    else:
        form = PostEditForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/edit-post.html', context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }

    return render(request, 'posts/details-post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dash')

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/delete-post.html', context)



# # Old index()
#
# def index(request):
#     form = PersonForm(request.POST or None)
#
#     if request.method == "POST":
#         print(request.POST['person_name'])
#
#     if form.is_valid():
#         print(form.cleaned_data['person_name'])
#
#     context = {
#         "my_form": form
#     }
#
#     return render(request, 'base.html', context)
#
#
#
#
# def index(request):
#     context = {
#         'current_time': datetime.now(),
#         'person': {
#             'name': 'Damien',
#             'age': 42,
#             'occupation': 'Unknown',
#         },
#         'ids': [
#             '6851268543',
#             'aosjdkadsd',
#             '46a8sd53ds',
#         ],
#         'some_text': 'this text is going to be used to display some of the Filters in the Django Template Language (DTL)',
#         'empty_text': '',
#         'users': [
#             'Pesho',
#             'Ivan',
#             'Stamat',
#             'Maria',
#             'Magdalena'
#         ]
#     }
#
#     return render(request, 'base.html', context)