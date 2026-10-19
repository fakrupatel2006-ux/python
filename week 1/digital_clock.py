from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.config(bg="skyblue")

clock = Label(root,
              font=("Arial", 40, "bold"),
              bg="skyblue",
              fg="darkblue")
clock.pack(pady=70)

def time():
    clock.config(text=strftime("%H:%M:%S %p"))
    clock.after(1000, time)

time()
root.mainloop()