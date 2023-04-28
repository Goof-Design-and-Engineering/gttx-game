import  os, subprocess

p = subprocess.Popen("python bot.py bot0@gttx.app bot0pass gqkvmzpivxxxz6o")
p2 = subprocess.Popen("python bot.py bot1@gttx.app bot1pass gqkvmzpivxxxz6o")


try:
    while(True):
        pass
except KeyboardInterrupt:
    print("Stopped.")
    p.terminate()
    p2.terminate()
    exit()