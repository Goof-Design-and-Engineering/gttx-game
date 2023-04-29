import  os, subprocess, json
from time import sleep

NUM_BOTS = 2
ROOM = "gqkvmzpivxxxz6o"
accounts = json.load(open("accounts.json", 'r'))

def process_line(line:str):
    line = line.rstrip("\n")
    line_list = line.split("\t")
    if (line_list[0] == "login"):
        login_file.write(line_list[2])
    elif (line_list[0] == "dashb"):
        dashb_file.write(line_list[2])
    elif (line_list[0] == "start"):
        start_file.write(line_list[2])

login_file = open("stats_login_"+str(NUM_BOTS), "a")
dashb_file = open("stats_dashb_"+str(NUM_BOTS), "a")
start_file = open("stats_start_"+str(NUM_BOTS), "a")


bots = []
for i in range(0,NUM_BOTS):
    bots.append(subprocess.Popen(("python bot.py " + accounts[i]["u"] + " " + accounts[i]["p"]+ " " + ROOM + " " + str(i)), stdout=subprocess.PIPE))
    sleep(0.1)


try:
    for i in range(0,NUM_BOTS):
        bots[i].wait()
        for line in bots[i].stdout:
            process_line(line.decode())

except KeyboardInterrupt:
    print("Stopped.")
    for i in range(0,NUM_BOTS):
        bots[i].terminate()
    exit()

print("finished")