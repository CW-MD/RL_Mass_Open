import pyautogui as pag
import tkinter as tk
from tkinter import messagebox
import time

width = pag.size().width
height = pag.size().height

def iterateBoxes(numItems):
    for i in range(numItems):
        pag.moveTo(width * .0781,height * .8550)
        time.sleep(.1)
        pag.moveTo(width * .0781, height * .8550)
        pag.click()
        pag.moveTo(width * .4425,height * .5750)
        time.sleep(.1)
        pag.moveTo(width * .4425, height * .5750)
        pag.click()
        pag.moveTo(width * .5300,height * .9300)
        time.sleep(7.60)
        pag.moveTo(width * .5300, height * .9300)
        pag.click()

def onButtonClick():
    try:
        value = int(entry.get())
        iterateBoxes(value)
    except ValueError:
        print(1)
        messagebox.showerror("Invalid Input", "Please enter a valid number")

root = tk.Tk()
root.anchor()
root.title("RL MassOpen")
#root.geometry("350x200+")
root.geometry('%dx%d+%d+%d' % (350, 200, (width * .8), (height * .1)))
label = tk.Label(root, text="# of items in one (selected) stack")
label.pack()
entry = tk.Entry(root)
entry.pack(pady=10)
info_text = "*For best results, Rocket League should be open in windowed mode on your primary monitor, with this program set somewhere near the top right corner of the same window"
info_label = tk.Label(root, text=info_text, wraplength=240, justify="left")
info_label.pack(pady=10)
button = tk.Button(root, text="Start Opening", command=onButtonClick)
button.pack(pady=10)
root.mainloop()
