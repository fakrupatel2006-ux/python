from tkinter import *
import random

WIDTH = 900
HEIGHT = 600

root = Tk()
root.title("PONG GAME")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="#020617")
root.resizable(False, False)

canvas = Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#020617",
    highlightthickness=0
)
canvas.pack()

# ===== Space Background =====

stars = []

for i in range(250):

    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(1,3)

    color = random.choice([
        "white",
        "#00FFFF",
        "#7DF9FF",
        "#FFD700"
    ])

    star = canvas.create_oval(
        x-size,
        y-size,
        x+size,
        y+size,
        fill=color,
        outline=""
    )

    stars.append(star)

# ===== Center Line =====

for i in range(0, HEIGHT, 25):

    canvas.create_rectangle(
        WIDTH//2-2,
        i,
        WIDTH//2+2,
        i+15,
        fill="#00FFFF",
        outline=""
    )

canvas.create_text(
    WIDTH//2,
    35,
    text="PONG GAME",
    fill="#00FFFF",
    font=("Verdana",30,"bold")
)

player_score = 0
computer_score = 0

score = canvas.create_text(
    WIDTH//2,
    75,
    text="0 : 0",
    fill="white",
    font=("Arial",22,"bold")
)

# ===== Ball =====

ball = canvas.create_oval(
    440,
    290,
    460,
    310,
    fill="white",
    outline="#00FFFF",
    width=2
)

ball_x = 10
ball_y = 10
speed = 7

# ===== Paddles =====

player = canvas.create_rectangle(
    30,
    220,
    45,
    360,
    fill="#00FFFF",
    outline=""
)

computer = canvas.create_rectangle(
    855,
    220,
    870,
    360,
    fill="#FF4444",
    outline=""
)

# ===== Smooth Controls =====

up = False
down = False

def key_press(event):
    global up, down

    if event.keysym == "Up":
        up = True

    elif event.keysym == "Down":
        down = True


def key_release(event):
    global up, down

    if event.keysym == "Up":
        up = False

    elif event.keysym == "Down":
        down = False


root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# ===== Reset Ball =====

def reset_ball():

    global ball_x, ball_y

    canvas.coords(ball, 440, 290, 460, 310)

    ball_x = random.choice([-10, 10])
    ball_y = random.choice([-9, -8, 8, 9])


# ===== Main Game =====

def game():

    global ball_x, ball_y
    global player_score, computer_score

    # ---------- Smooth Player Movement ----------

    if up:
        x1, y1, x2, y2 = canvas.coords(player)
        if y1 > 0:
            canvas.move(player, 0, -18)

    if down:
        x1, y1, x2, y2 = canvas.coords(player)
        if y2 < HEIGHT:
            canvas.move(player, 0, 18)

    # ---------- Ball ----------

    canvas.move(ball, ball_x, ball_y)

    bx1, by1, bx2, by2 = canvas.coords(ball)

    px1, py1, px2, py2 = canvas.coords(player)
    cx1, cy1, cx2, cy2 = canvas.coords(computer)

    # ---------- Top & Bottom ----------

    if by1 <= 0 or by2 >= HEIGHT:
        ball_y = -ball_y

    # ---------- Player Paddle ----------

    if bx1 <= px2 and py1 < by2 and py2 > by1:

        ball_x = abs(ball_x) + 0.4

    # ---------- Computer Paddle ----------

    if bx2 >= cx1 and cy1 < by2 and cy2 > by1:

        ball_x = -(abs(ball_x) + 0.4)

    # ---------- Player Scores ----------

    if bx2 >= WIDTH:

        player_score += 1

        canvas.itemconfig(
            score,
            text=f"{player_score}  :  {computer_score}"
        )

        reset_ball()

    # ---------- Computer Scores ----------

    if bx1 <= 0:

        computer_score += 1

        canvas.itemconfig(
            score,
            text=f"{player_score}  :  {computer_score}"
        )

        reset_ball()
        
            # ===== Computer AI =====

    _, cy1, _, cy2 = canvas.coords(computer)

    computer_center = (cy1 + cy2) / 2
    ball_center = (by1 + by2) / 2

    # Smart AI
    if computer_center < ball_center - 10 and cy2 < HEIGHT:
        canvas.move(computer, 0, 14)

    elif computer_center > ball_center + 10 and cy1 > 0:
        canvas.move(computer, 0, -14)

    # ===== Winner =====

    if player_score == 3:
    
        canvas.create_text(
            WIDTH//2,
            HEIGHT//2,
            text="🏆 YOU WIN 🏆",
            fill="#00FF66",
            font=("Verdana",36,"bold"),
            tags="winner"
        )

        canvas.create_text(
            WIDTH//2,
            HEIGHT//2+60,
            text="Press R to Restart",
            fill="white",
            font=("Arial",18),
            tags="winner"
        )

        return

    if computer_score == 3:

        canvas.create_text(
            WIDTH//2,
            HEIGHT//2,
            text="GAME OVER",
            fill="#FF4444",
            font=("Verdana",36,"bold"),
            tags="winner"
        )

        canvas.create_text(
            WIDTH//2,
            HEIGHT//2+60,
            text="Press R to Restart",
            fill="white",
            font=("Arial",18),
            tags="winner"
        )

        return

    root.after(speed, game)


# ===== Restart =====

def restart(event=None):

    global player_score
    global computer_score

    player_score = 0
    computer_score = 0

    canvas.delete("winner")

    canvas.itemconfig(
        score,
        text="0 : 0"
    )

    canvas.coords(player,30,220,45,360)
    canvas.coords(computer,855,220,870,360)

    reset_ball()

    game()


root.bind("r", restart)
root.bind("R", restart)

# ===== Animated Background =====

def animate_background():

    for star in stars:

        canvas.move(star, -3, 0)

        x1, y1, x2, y2 = canvas.coords(star)

        if x2 < 0:

            new_y = random.randint(0, HEIGHT)
            size = random.randint(1,3)

            canvas.coords(
                star,
                WIDTH,
                new_y,
                WIDTH+size,
                new_y+size
            )

    root.after(30, animate_background)


# ===== Glowing Effect =====

def glow():

    colors = [
        "#00FFFF",
        "#00FF99",
        "#7DF9FF",
        "#FFFFFF",
        "#FFD700"
    ]

    color = random.choice(colors)

    canvas.itemconfig(player, fill=color)
    canvas.itemconfig(ball, outline=color)

    root.after(150, glow)


# ===== Footer =====

canvas.create_text(
    WIDTH//2,
    HEIGHT-20,
    text="↑ / ↓  Move Paddle      R Restart      First to 3 Wins",
    fill="#CCCCCC",
    font=("Arial",12,"bold")
)


# ===== Countdown =====

count = canvas.create_text(
    WIDTH//2,
    HEIGHT//2,
    text="3",
    fill="white",
    font=("Verdana",60,"bold")
)


def start_game(n):

    if n == 0:

        canvas.delete(count)

        animate_background()

        glow()

        game()

        return

    canvas.itemconfig(count, text=str(n))

    root.after(1000, lambda: start_game(n-1))


# ===== Start Game =====

reset_ball()

start_game(3)

root.mainloop()