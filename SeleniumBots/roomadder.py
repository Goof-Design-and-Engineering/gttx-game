import json
from pocketbase import PocketBase

ROOM_ID = "732idvo8nsob4ut" 
ORG_ID = "7z9ag8na0pfubxk"

client = PocketBase('https://api.gttx.app')
with open("creds.txt", "r") as creds:
    #creds.gitignore is a file with two lines in it. line 0 is the username, line 1 is the password.
    admin_data = client.admins.auth_with_password(creds.readline().replace("\n", ""), creds.readline().replace("\n", ""))

org = client.collection("organization").get_one(ORG_ID)
room = client.collection("room").get_one(ROOM_ID)

users = []

for user in org.members:
    users.append(user)

room_update = {
    "org" : ORG_ID,
    "users" : users,
    "scenarios" : room.scenarios
}

client.collection("room").update(ROOM_ID, room_update)