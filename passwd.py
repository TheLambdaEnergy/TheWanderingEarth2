import tkinter as tk
import tkinter.ttk as ttk
import time

text2 = '''信息:root.planetengine.jp
502 Bad Gateway (HTTP 6.1)
us.root.planetengine.com
502 Bad Gateway (HTTP 6.1)
响应了未使用的数据:
<jntm jnszstm>
'''

text3 = '''CPU:CSU Quantum 970 6.7 Zhz
GPU:(1)NVIDIA(R) A10000
    (2)CSU Quantum Render 320X 1TB
HardDrive:UEG-TPM 
          Quantum 550W 324TB/10ZB
Displayer:IBM QuantumLCD
Net:Ethernet 
'''

top = tk.Tk()
top.geometry("600x100+120+400")
top.title("550W UEG Connection")
top.config(background="#000000")
top.attributes('-topmost', True)
pgval = 96

lb1 = tk.Label(top, text="UEG 服务器连接:{}%".format(pgval), fg="#FFFFFF", bg="#000000")
lb2 = tk.Label(top, text="Time remaining :3min")
progressbar = ttk.Progressbar(top, length=550)
progressbar['maximum'] = 100
progressbar['value'] = pgval

lb1.pack()
progressbar.pack()

win1 = tk.Toplevel(top, bg="#000000")
win1.attributes("-toolwindow", True)
win1.geometry("250x250+100+50")
win1.title("!   WARNING   !")
winlb1 = tk.Label(win1, bg="#000000", fg="#F2481B",
                  text="UEG 信息:月球碎片将于\n3分钟后降落.\n请将伺服器连接到\n 全球网络系统.",
                  font=("微软雅黑", 12))
winlb1.pack(fill="both")

win2 = tk.Toplevel(top, bg="#000000")
win2.attributes("-toolwindow", True)
win2.geometry("250x250+410+50")
win2.title("1145141919810")
winlb2 = tk.Label(win2, bg="#000000", fg="#FFFFFF",
                  text=text2,
                  font=("微软雅黑", 12))
winlb2.pack(fill="both")

win3 = tk.Toplevel(top, bg="#000000")
win3.attributes("-toolwindow", True)
win3.geometry("250x250+720+50")
win3.title("550W infomation")
winlb3 = tk.Label(win3, bg="#000000", fg="#00FFFF",
                  text=text3,
                  font=("Consolas", 12))
winlb3.pack(fill="both")

win4 = tk.Toplevel(top, bg="#000000")
win4.geometry("300x300+160+90")
win4.attributes("-topmost", True)
winlb4 = tk.Label(win4, bg="#000000", fg="#FFFFFF", text="Type password of 100 characters")
winf = tk.Frame(win4, bg="#000000")
winf.pack()
winlb4.pack()
order = 0
for y in range(10):
    for x in range(10):
        exec(
            f"""word{order} = tk.Label(winf,bg='orange',fg='white',width=3,text=" ");word{order}.grid(row={y},column={x},padx=1,pady=1)
""")
        order += 1


def reset():
    global order
    for i in range(100):
        exec(f"word{i}.config(text=' ')")
    order = 0


winbtn1 = tk.Button(win4, bg="orange", fg="white", text="RESET", command=reset)
winbtn1.pack()
order = 0


def complete():
    lb1.config(text="完成!")
    for i in range(4):
        progressbar['value'] += 1
        time.sleep(0.03)
        top.update()
    win1.destroy()
    win2.destroy()
    win3.destroy()
    win4.destroy()
    # print("Password correct.")
    time.sleep(5)
    top.destroy()
    print("[Subprocess message]exit")
    time.sleep(5)


def eventHandler(event):
    global order
    if order >= 100:
        complete()
        return
    # print(event.char)
    char = event.char
    if char not in "1234567890":
        return
    exec(f"word{order}.config(text=char)")
    order += 1


win4.bind("<Key>", eventHandler)

top.mainloop()
