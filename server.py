import time
import subprocess
# from tkinter import messagebox
import random


# import unicurses as curses

def addmsg(msg, color="white", wait=0.1):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")

    time.sleep(wait)


print("""
====================================================================
 ____  ___   ___
/     /    / *  0      W THE INTELIGENT QUANTUM COMPUTER
^==-5 ^== 5|  *   W   W       550W (MOSS)
     5     0   * W W W   COPYRIGHT 1978-2044 UNITED EARTH GOVERNMENT
5555  5555  0000W   W
====================================================================
STARTING...
""")

time.sleep(2)
addmsg("Found hardware in /dev: (1) Beijing Root Server Terminal")
addmsg("Generating operating system...")
time.sleep(4)

addmsg("Connected to DNS server.", color="aqua")
addmsg("Trying to connect to Tokyo server")
addmsg("Requested data to root.planetengine.jp", color="aqua", wait=1)
load = 0
while load <= 100:
    addmsg("Retriving server keys... " + str(load) + "%", wait=1)
    add = random.randint(1, 15)
    load += add

addmsg("Done.")

addmsg("Trying to connect to Dulles server")
addmsg("Requested data to us.root.planetengine.com", color="aqua", wait=1)
load = 0
while load <= 100:
    addmsg("Retriving server keys... " + str(load) + "%", wait=1)
    add = random.randint(1, 15)
    load += add

addmsg("Done.")
time.sleep(5)

'''
stdscr = curses.initscr()
curses.cberak()
curses.noecho()
stdscr.keypad(1)
win = curses.newwin(10,50,0,0)
'''
# messagebox.askokcancel("Upload data to 550W?")

addmsg("Now compiling kernel code")
addmsg("Found compiler <550U basic operating system kernel compiler>", wait=2)
addmsg("WARNING!Compiler outdated", color="yellow")

proc = subprocess.Popen(args=["python", "passwd.py"], shell=False, stdout=subprocess.PIPE)

with open("textwrap.txt", "r") as f:
    for line in f:
        code = line.rstrip()
        if code.strip().startswith("#"):
            addmsg(code, color="green", wait=0.05)
        elif code.strip().startswith(">>>"):
            addmsg(code, color="yellow", wait=0.05)
        elif code.strip().startswith('"""'):
            addmsg(code, color="red", wait=0.05)
        else:
            addmsg(code, color="aqua", wait=0.05)

addmsg("\n\nCompile Finished!", color="aqua")
addmsg("Uncaught Error: user <root> password outdated,need to verify", color="red")
addmsg("Waiting for subprocess password typing...")

while 1:
    try:
        output, err = proc.communicate()
        result = output.decode('gbk')
        addmsg(result, color="yellow")
        if result == '[Subprocess message]exit\r\n':
            proc.terminate()
            break
    except:
        pass
addmsg("Subprocess exit code:" + str(proc.poll()))
addmsg("Successfully to connect to Global Internet!")
addmsg("GET 1 verified command:ueg_planetengnine_launch")
addmsg("Launching Planet Engine in Asia-NorthAmerica-6-132", wait=3)
addmsg("Success!")

input("Press Enter to exit.")
