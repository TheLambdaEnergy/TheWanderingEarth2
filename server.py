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
/     /    / *  0      W       智能量子计算机
^==-5 ^== 5|  *   W   W       550W (MOSS)
     5     0   * W W W   COPYRIGHT 1978-2077 地球联合政府
5555  5555  0000W   W
====================================================================
启动中...
""")

time.sleep(2)
addmsg("在 /dev 找到 1 设备: (1) 北京根服务器控制台")
addmsg("正在生成底层操作系统...")
time.sleep(4)

addmsg("已连接到DNS服务器.", color="aqua")
addmsg("尝试连接到位于 东京 的服务器:")
addmsg("正在向 root.planetengine.jp 请求数据", color="aqua", wait=1)
load = 0
while load <= 100:
    addmsg("检索服务器密钥... " + str(load) + "%", wait=1)
    add = random.randint(1, 15)
    load += add

addmsg("Done.")

addmsg("尝试连接到位于 杜勒斯 的服务器")
addmsg("正在向 us.root.planetengine.com 请求数据", color="aqua", wait=1)
load = 0
while load <= 100:
    addmsg("检索服务器密钥... " + str(load) + "%", wait=1)
    add = random.randint(1, 15)
    load += add

addmsg("完成.")
time.sleep(5)

'''
stdscr = curses.initscr()
curses.cberak()
curses.noecho()
stdscr.keypad(1)
win = curses.newwin(10,50,0,0)
'''
# messagebox.askokcancel("Upload data to 550W?")

addmsg("开始编译发动机控制程序内核")
addmsg("命中 <550U basic operating system kernel compiler> 位于 /usr/kernel", wait=2)
addmsg("WARNING警告!编译程序已过期", color="yellow")

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

addmsg("\n\n编译完成!", color="aqua")
addmsg("未知错误: 用户 <root> 密码信息已过期,需要验证", color="red")
addmsg("等待子进程密码输入...")

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
addmsg("子进程结束码:" + str(proc.poll()))
addmsg("成功连接到全球网络!")
addmsg("收到 1 个已验证的命令:ueg_planetengnine_launch")
addmsg("正在启动位于 亚洲-北美洲-6-132 的行星发动机", wait=3)
addmsg("成功!")

input("按下回车退出.")
