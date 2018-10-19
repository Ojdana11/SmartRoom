from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'dashboard/index.html', {})

def room(request, room_name):
    return render(request, 'dashboard/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
    