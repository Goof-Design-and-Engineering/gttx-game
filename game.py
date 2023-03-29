from pb_lib import *
from game_html import *
from flask import Flask, request
import requests, asyncio, json

class RoomInstance():
    def __init__(self, id):
        self.room = pullRoom(id)
        self.scenario = client.collection("scenario").get_one(self.room.scenarios).contents


open_rooms = {}

app = Flask(__name__)

@app.route('/start/<id>')
def start(id):
    if id not in open_rooms and checkRoom(id):
        open_rooms[id] = RoomInstance(id)
        print("Opened room:  "+id)
        return game(id)
    elif id in open_rooms:
        return game(id)
    else:
        return "No :)"

@app.route('/game/<id>')
def game(id):
    if id in open_rooms:
        return request_game.replace("%GAMEJSON%", json.dumps(open_rooms[id].scenario))
    else:
        return "No :)"

@app.route('/close/<id>')
def close(id):
     if id in open_rooms:
         open_rooms.pop(id)
         print("Closed room:  "+id)
         return "Room Closed"
     else:
         return "No :)"

@app.route('/cookie')
def cookie():
    return request.cookies

@app.route('/')
def index():
    return request_game

if __name__ == '__main__':
    app.run()