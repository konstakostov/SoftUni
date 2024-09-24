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
        'empty_text': ''
    }

    return render(request, 'base.html', context)