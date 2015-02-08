from django.shortcuts import render

# Create your views here.

from django.http import StreamingHttpResponse, HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from rooms.models import Room
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from rooms import getGlobalCopy, updateGlobalRuntimeRoom

def hello(request):
    G = getGlobalCopy();
    rooms = G.db["rooms"]
    t = get_template('index.html')
    for room in rooms:
        room.players = "%s/%s" % (2, room.maxplayer)
        room.ping = 10
    c = Context({"rooms": rooms})
    print(request)
    return HttpResponse(t.render(c))

@ensure_csrf_cookie
def room_details(request):
    if request.method == 'GET':
        if request.GET['type'] == 'room_details':
            print(request.GET['room_name'])
    G = getGlobalCopy();
    roomname = "room1"
    roomdata = {"players":[{"player":"player1","ping":"3"}, {"player":"player2","ping":"33"}], "host":""}
    newroom = (roomname, roomdata)
    updateGlobalRuntimeRoom(newroom)
    dumps = json.dumps(G.runtime["rooms"][request.GET['room_name']]["players"])
    #dumps = json.dumps([{"player":"player1","ping":"3"}, {"player":"player2","ping":"33"}])
    print(dumps)
    return StreamingHttpResponse(dumps)
