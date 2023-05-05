import json
from pocketbase import PocketBase

ORG_ID = "7z9ag8na0pfubxk"
MINACC = 0
MAXACC = 100
PASSLEFT = ""
PASSRIGHT = ""




client = PocketBase('https://api.gttx.app')
with open("creds.txt", "r") as creds:
    #creds.gitignore is a file with two lines in it. line 0 is the username, line 1 is the password.
    admin_data = client.admins.auth_with_password(creds.readline().replace("\n", ""), creds.readline().replace("\n", ""))

x = []

organization = client.collection("organization").get_one(ORG_ID)
for i in range(MINACC, MAXACC):
    result = client.collection("users").create({
        "username" : "Bot"+str(i),
        "name" : "Bot #"+str(i),
        "role": "participant",
        "email" : "bot"+str(i)+"@gttx.app",
        "password" : PASSLEFT+str(i)+PASSRIGHT,
        "passwordConfirm": PASSLEFT+str(i)+PASSRIGHT,
        "org" : ORG_ID})
    organization.members.append(result.id)
    x.append({"u" : result.email, "p" : "bot"+str(i)+"pass"})

with open('accounts.json', 'w', encoding='utf-8') as f:
    json.dump(x, f, ensure_ascii=False, indent=4)

members = {"members" : [], "name" : "Bot Business Group"}
for member in organization.members:
    members["members"].append(member)
client.collection("organization").update(ORG_ID, members)