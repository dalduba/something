from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from rooms.models import Room

def hello(request):
    rooms = Room.objects.all()
    t = get_template('index.html')
    c = Context({"rooms": rooms})
    print(t.render(c))
    return HttpResponse(t.render(c))
