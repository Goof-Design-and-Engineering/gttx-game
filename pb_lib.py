from pocketbase import PocketBase

#A lot of these functions will be basically renaming the functions.
def pullRoom(id):
    return client.collection("room").get_one(id)

def updateRoom(room, item, value):
    client.collection("room").update(room.id, {item: value})

def checkRoom(id):
    try:
        client.collection("room").get_one(id)
        return True
    except:
        return False


#Log into the database as an admin
client = PocketBase('https://api.gttx.app')
with open("creds.txt", "r") as creds:
    #creds.gitignore is a file with two lines in it. line 0 is the username, line 1 is the password.
    admin_data = client.admins.auth_with_password(creds.readline().replace("\n", ""), creds.readline().replace("\n", ""))

id = "81lp924dbt8riiy"
print(checkRoom(id))