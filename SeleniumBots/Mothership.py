import  os, subprocess, json
from time import sleep

DELAY = 1
NUM_BOTS = 100
ROOM = "732idvo8nsob4ut"
accounts = json.load(open("accounts.json", 'r'))



bots = []
for i in range(0,NUM_BOTS):
    bots.append(subprocess.Popen(("python bot.py " + accounts[i]["u"] + " " + accounts[i]["p"]+ " " + ROOM + " " + str(i)), stdout=subprocess.PIPE))
    sleep(DELAY)


try:
    for i in range(0,NUM_BOTS):
        bots[i].wait()

except KeyboardInterrupt:
    print("Stopped.")
    for i in range(0,NUM_BOTS):
        bots[i].terminate()
    exit()

print("finished")