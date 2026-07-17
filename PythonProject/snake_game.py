import turtle
import time
import random

# Base configurations
NORMAL_SPEED = 0.12  # Steady, relaxed pace
FAST_SPEED = 0.06    # Challenging pace
current_delay = NORMAL_SPEED

score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game - Timepass Edition")
wn.bgcolor("black")
wn.setup(width=600, height=650)  # Made slightly taller for the button
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, -20)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 80)

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# --- SPEED BUTTON SYSTEM ---
button = turtle.Turtle()
button.speed(0)
button.color("white", "darkblue")  # White text/border, blue background
button.penup()
button.hideturtle()
button.goto(0, 280)  # Positioned at the very top

def draw_button(text):
    button.clear()
    # Draw button background box
    button.goto(-90, 275)
    button.begin_fill()
    for _ in range(2):
        button.forward(180)
        button.left(90)
        button.forward(35)
        button.left(90)
    button.end_fill()
    # Write text inside the box
    button.goto(0, 283)
    button.write(text, align="center", font=("Courier", 14, "bold"))

# Initialize the button text
draw_button("Speed: NORMAL")

def change_speed(x, y):
    global current_delay
    # Check if the click happened inside the button box
    if -90 <= x <= 90 and 275 <= y <= 310:
        if current_delay == NORMAL_SPEED:
            current_delay = FAST_SPEED
            draw_button("Speed: FAST 🔥")
        else:
            current_delay = NORMAL_SPEED
            draw_button("Speed: NORMAL")

# Listen for mouse clicks on the screen
wn.onclick(change_speed)
# ----------------------------

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border (Adjusted top border for scoreboard/button)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 230 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, -20)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 220)  # Keep food below the scoreboard
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, -20)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(current_delay)

wn.mainloop()