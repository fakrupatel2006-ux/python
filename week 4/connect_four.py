from tkinter import *
from tkinter import messagebox

ROWS = 6
COLS = 7
SIZE = 80

root = Tk()
root.title("Connect Four")
root.geometry(f"{COLS*SIZE}x{ROWS*SIZE+150}")
root.configure(bg="#081C3A")

current = "Red"

board = [["" for _ in range(COLS)] for _ in range(ROWS)]
cells = []

title = Label(
    root,
    text="CONNECT FOUR",
    font=("Verdana",28,"bold"),
    bg="#081C3A",
    fg="gold"
)
title.pack(pady=10)

turn = Label(
    root,
    text="Turn : Red",
    font=("Arial",16,"bold"),
    bg="#081C3A",
    fg="white"
)
turn.pack()

frame = Frame(
    root,
    bg="#1E4E8C",
    bd=8,
    relief="ridge"
)
frame.pack(pady=20)


def check(color):

    for r in range(ROWS):
        for c in range(COLS-3):
            if all(board[r][c+i]==color for i in range(4)):
                return True

    for r in range(ROWS-3):
        for c in range(COLS):
            if all(board[r+i][c]==color for i in range(4)):
                return True

    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i]==color for i in range(4)):
                return True

    for r in range(3,ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i]==color for i in range(4)):
                return True

    return False


def draw():

    for r in range(ROWS):
        for c in range(COLS):

            if board[r][c]=="Red":
                color="red"

            elif board[r][c]=="Yellow":
                color="yellow"

            else:
                color="white"

            cells[r][c].config(bg=color)


def restart():

    global board,current

    board=[["" for _ in range(COLS)] for _ in range(ROWS)]

    current="Red"

    turn.config(text="Turn : Red")

    draw()


def click(event):

    global current

    col=event.widget.grid_info()["column"]

    for row in range(ROWS-1,-1,-1):

        if board[row][col]=="":

            board[row][col]=current

            draw()

            if check(current):

                messagebox.showinfo("Winner",current+" Wins!")

                restart()

                return

            if all("" not in r for r in board):

                messagebox.showinfo("Draw","Match Draw!")

                restart()

                return

            current="Yellow" if current=="Red" else "Red"

            turn.config(text="Turn : "+current)

            return


for r in range(ROWS):

    row=[]

    for c in range(COLS):

        lbl=Label(
            frame,
            width=6,
            height=3,
            bg="white",
            relief="raised",
            bd=3
        )

        lbl.grid(row=r,column=c,padx=4,pady=4)

        lbl.bind("<Button-1>",click)

        row.append(lbl)

    cells.append(row)

footer=Label(
    root,
    text="Python Connect Four Game",
    font=("Arial",10),
    bg="#081C3A",
    fg="lightgray"
)
footer.pack(pady=8)

draw()

root.mainloop()