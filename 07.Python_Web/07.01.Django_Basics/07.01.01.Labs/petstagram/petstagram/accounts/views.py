from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'accounts/login-page.html')


def profile_delete_page(request):
    return render(request, 'accounts/profile-delete-page.html')


def profile_details_page(request):
    return render(request, 'accounts/profile-details-page.html')


def profile_edit_page(request):
    return render(request, 'accounts/profile-edit-page.html')


def register_page(request):
    return render(request, 'accounts/register-page.html')
