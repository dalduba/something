from rooms.models import Room
import copy
import mutex

class Global():
    db = {"rooms":{}}
    runtime = {"rooms":{}}

G = Global()

def initGlobal():
    rooms = Room.objects.all()
    G.db["rooms"] = copy.deepcopy(rooms)
    for room in G.db["rooms"]:
        G.runtime["rooms"][room.name] = {"players":[], "host":""}

def getGlobalCopy():
    return copy.deepcopy(G)

def updateGlobalRuntimeRoom(room):
    name, data = room
    G.runtime["rooms"][name] = copy.deepcopy(data)
    #     G.runtime["rooms"][name][key] = value
    # print(G.runtime["rooms"])

initGlobal()