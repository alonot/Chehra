import subprocess
import os
import sys

os.system("python " + os.path.join(sys._MEIPASS, "setup.py"))

def start():
    print("starting")
    os.system("python " + os.path.join(sys._MEIPASS, "main.py"))

start()

# subprocess.call(["python","setup.py"])
