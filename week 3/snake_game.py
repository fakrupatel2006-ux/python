from tkinter import *
import random

WIDTH = 600
HEIGHT = 400
SIZE = 20
SPEED = 150

root = Tk()
root.title("Snake Game")
root.resizable(False, False)

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="#222222")
canvas.pack()

score = 0

score_text = Label(root, text="Score: 0", font=("Arial", 14, "bold"))
score_text.pack()

snake = [(100, 100)]
direction = "Right"

food = (
    random.randint(0, (WIDTH-SIZE)//SIZE) * SIZE,
    random.randint(0, (HEIGHT-SIZE)//SIZE) * SIZE
)

def draw():
    canvas.delete("all")

    canvas.create_rectangle(
        food[0], food[1],
        food[0]+SIZE, food[1]+SIZE,
        fill="red"
    )

    for part in snake:
        canvas.create_rectangle(
            part[0], part[1],
            part[0]+SIZE, part[1]+SIZE,
            fill="lime"
        )

def move():

    global food, score

    x, y = snake[0]

    if direction == "Up":
        y -= SIZE

    elif direction == "Down":
        y += SIZE

    elif direction == "Left":
        x -= SIZE

    elif direction == "Right":
        x += SIZE

    head = (x, y)

    if (
        x < 0 or
        x >= WIDTH or
        y < 0 or
        y >= HEIGHT or
        head in snake
    ):
        game_over()
        return

    snake.insert(0, head)

    if head == food:

        score += 1

        score_text.config(text="Score: "+str(score))

        food = (
            random.randint(0,(WIDTH-SIZE)//SIZE)*SIZE,
            random.randint(0,(HEIGHT-SIZE)//SIZE)*SIZE
        )

    else:
        snake.pop()

    draw()

    root.after(SPEED, move)

def change(event):

    global direction

    if event.keysym == "Up" and direction != "Down":
        direction = "Up"

    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"

    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"

    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"

def game_over():

    canvas.create_text(
        WIDTH//2,
        HEIGHT//2,
        text="GAME OVER\nPress R to Restart",
        fill="white",
        font=("Arial",24,"bold")
    )

def restart(event):

    global snake, direction, food, score

    snake = [(100,100)]
    direction = "Right"
    score = 0

    score_text.config(text="Score: 0")

    food = (
        random.randint(0,(WIDTH-SIZE)//SIZE)*SIZE,
        random.randint(0,(HEIGHT-SIZE)//SIZE)*SIZE
    )

    draw()

    move()

root.bind("<Up>", change)
root.bind("<Down>", change)
root.bind("<Left>", change)
root.bind("<Right>", change)
root.bind("r", restart)
root.bind("R", restart)

draw()
move()

root.mainloop()