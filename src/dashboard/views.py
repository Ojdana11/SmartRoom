from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'dashboard/index.html', {})

    