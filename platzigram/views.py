"""Platzigram views."""
from django.http import HttpResponse
from datetime import datetime
import json 


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sortedNumbers = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sortedNumbers,
        'message': 'Integers sorted succesfully.'
    }

    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
        )  



def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to platzigram'.format(name)

    return HttpResponse(message)

