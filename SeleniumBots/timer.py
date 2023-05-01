import  os, subprocess, json
from time import sleep

NUM_BOTS = 100

accounts = json.load(open("accounts.json", 'r'))

def process_line(line:str):
    try:
        #print(line)
        line = line.rstrip('\n')
        line_list = line.split("\t")
        with open(str(NUM_BOTS)+"_"+line_list[0]+".txt", 'a') as f:
            f.write(str(line_list[1]))
    except Exception as e:
        print(e)
   



for j in range(0, 100//NUM_BOTS):
    bots = []
    for i in range(0,NUM_BOTS):
        bots.append(subprocess.Popen(("python timerbot.py " + accounts[i]["u"] + " " + accounts[i]["p"]), stdout=subprocess.PIPE))
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

    print("finished run "+str(j))