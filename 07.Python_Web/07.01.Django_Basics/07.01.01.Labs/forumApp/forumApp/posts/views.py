from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'current_time': datetime.now(),
        'person': {
            'name': 'Damien',
            'age': 42,
            'occupation': 'Unknown',
        },
        'ids': [
            '6851268543',
            'aosjdkadsd',
            '46a8sd53ds',
        ],
        'some_text': 'this text is going to be used to display some of the Filters in the Django Template Language (DTL)',
        'empty_text': '',
        'users': [
            'Pesho',
            'Ivan',
            'Stamat',
            'Maria',
            'Magdalena'
        ]
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        'posts': [
            {
                'title': 'How to create a Django Project - Version 01',
                'author': 'Bob Johnson',
                'content': 'I really don\'t know how to use the Django Framework',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create a Django Project - Version 02',
                'author': 'Don Johnson',
                'content': 'I really don\'t know what us Django',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create a Django Project - Version 02',
                'author': 'Ron Johnson',
                'content': 'I really don\'t.',
                'created_at': datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)