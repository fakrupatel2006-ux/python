from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")
root.configure(bg="#1e3a5f")

player = "X"

title = Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 24, "bold"),
    bg="#1e3a5f",
    fg="white"
)
title.pack(pady=20)

frame = Frame(root, bg="#1e3a5f")
frame.pack(expand=True)

def click(btn):
    global player

    if btn["text"] == "":
        btn["text"] = player

        if player == "X":
            player = "O"
        else:
            player = "X"

        check_winner()

def check_winner():

    wins = [
        [b1,b2,b3],
        [b4,b5,b6],
        [b7,b8,b9],
        [b1,b4,b7],
        [b2,b5,b8],
        [b3,b6,b9],
        [b1,b5,b9],
        [b3,b5,b7]
    ]

    # Check Winner
    for row in wins:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            messagebox.showinfo(
                "Winner",
                row[0]["text"] + " Wins!"
            )
            reset()
            return

    # Check Draw
    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo(
            "Draw",
            "TIE ! would you like to restart the game?"
        )
        reset()

def reset():
    global player

    player = "X"

    for btn in buttons:
        btn["text"] = ""

b1 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b1)
)

b2 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b2)
)

b3 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b3)
)

b4 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b4)
)

b5 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b5)
)

b6 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b6)
)

b7 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b7)
)

b8 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b8)
)

b9 = Button(
    frame,
    font=("Arial",22,"bold"),
    width=5,
    height=2,
    bg="white",
    command=lambda: click(b9)
)

buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

b1.grid(row=0,column=0,padx=5,pady=5)
b2.grid(row=0,column=1,padx=5,pady=5)
b3.grid(row=0,column=2,padx=5,pady=5)

b4.grid(row=1,column=0,padx=5,pady=5)
b5.grid(row=1,column=1,padx=5,pady=5)
b6.grid(row=1,column=2,padx=5,pady=5)

b7.grid(row=2,column=0,padx=5,pady=5)
b8.grid(row=2,column=1,padx=5,pady=5)
b9.grid(row=2,column=2,padx=5,pady=5)

root.mainloop()