import  os, subprocess
from time import sleep

NUM_BOTS = 100


def process_line(line:str):
    global bots_started, bots_finished
    line = line.rstrip("\n")
    if "start" in line:
        bots_started += 1
    elif "finished" in line:
        bots_finished += 1

started = False
bots_started = 0
bots_finished = 0
bots =[]
for i in range(0,NUM_BOTS):
    bots.append(subprocess.Popen("python gridtest.py", stdout=subprocess.PIPE))

try:
    for i in range(0,NUM_BOTS):
        for line in bots[i].stdout:
            process_line(line.decode())
   
except KeyboardInterrupt:
    for i in range(0,NUM_BOTS):
        bots[i].terminate()
    exit()

print()
print("Started/Finished/Total Bots\t" + str(bots_started)+"/"+str(bots_finished)+"/"+str(NUM_BOTS))
print()