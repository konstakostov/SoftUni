from audioop import reverse

from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from djangoUrlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f"<h1>{url_lazy}</h1>")

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")

def view_with_name(request, variable):  # Should be named the same way as in urls
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {"variable": variable})

def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")


def view_with_slug(request, pk, slug):
    # # Option 01 for Error 404
    # department = Department.objects.get(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404
    #
    # return HttpResponse(f"<h1>Department from slug: {department.first()}</h1>")

    # Option 02 for Error 404
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponseNotFound()
    # return HttpResponse(status=404)   # Equal to the line above

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

# # NOT A GOOD IMPLEMENTATION → Breaks Abstraction
# def redirect_to_view(request):
#     return redirect('http://localhost:8000')

# # An OK Implementation → Breaks SR if view is from another app
# def redirect_to_view(request):
#     return redirect(index)

# Best Implementation
def redirect_to_view(request):
    return redirect('home')