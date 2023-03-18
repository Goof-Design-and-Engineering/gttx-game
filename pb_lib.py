from pocketbase import PocketBase

#This will be either in this file or app.py
class RoomInstance():
    pass

#A lot of these functions will be basically renaming the functions.
def pullRoom(id):
    return client.collection("room").get_one(id)

def updateRoom(room, item, value):
    client.collection("room").update(room.id, {item: value})


#Log into the database as an admin
client = PocketBase('https://api.gttx.app')
with open("creds.txt", "r") as creds:
    #creds.gitignore is a file with two lines in it. line 0 is the username, line 1 is the password.
    admin_data = client.admins.auth_with_password(creds.readline().replace("\n", ""), creds.readline().replace("\n", ""))

#example run
#result = pullRoom("u7c9u8f90mp067l")
#updateRoom(result, "uniqueid", "6969696969696969")