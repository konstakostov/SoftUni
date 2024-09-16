from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")

def view_with_name(request, variable):  # Should be named the same way as in urls
    return HttpResponse(f"<h1>Variable: {variable}</h1>")


def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")
