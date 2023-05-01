import  os, subprocess, json
from time import sleep

NUM_BOTS = 2
ROOM = "gqkvmzpivxxxz6o"
accounts = json.load(open("accounts.json", 'r'))



bots = []
for i in range(0,NUM_BOTS):
    bots.append(subprocess.Popen(("python bot.py " + accounts[i]["u"] + " " + accounts[i]["p"]+ " " + ROOM), stdout=subprocess.PIPE))
    sleep(0.1)


try:
    for i in range(0,NUM_BOTS):
        bots[i].wait()

except KeyboardInterrupt:
    print("Stopped.")
    for i in range(0,NUM_BOTS):
        bots[i].terminate()
    exit()

print("finished")