from tkinter import Tk, Canvas, Label
import random
from playsound3 import playsound

# --- Game settings ---
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100             # Delay (ms) between moves
SPACE_SIZE = 20
INITIAL_BODY_SIZE = 3

# Colors
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"

# Global game state
direction = 'down'
score = 0
after_job = None
game_over_sound = None

# --- Tkinter setup ---
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score_label = Label(window, text=f"Score: {score}", font=('consolas', 24))
score_label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BG_COLOR)
canvas.pack()

# --- Game object classes ---
class Snake:
    def __init__(self):
        self.body_size = INITIAL_BODY_SIZE
        self.coordinates = [(0, 0)] * self.body_size

        self.squares = []
        for (x, y) in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)



class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = (x, y)
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# --- Game logic functions ---
def next_turn(snake, food):
    global after_job, direction, score
    x, y = snake.coordinates[0]
    # Move head
    if direction == "up":    y -= SPACE_SIZE
    if direction == "down":  y += SPACE_SIZE
    if direction == "left":  x -= SPACE_SIZE
    if direction == "right": x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Check food collision
    if (x, y) == food.coordinates:
        game_over_sound = playsound("./assets/eat.mp3", block=False)
        score += 1
        score_label.config(text=f"Score: {score}")
        canvas.delete("food")
        #food = Food()
        while(True):
            food = Food()
            if food.coordinates in snake.coordinates:
                canvas.delete("food")
            else:
                break

    else:
        canvas.delete(snake.squares[-1])
        snake.squares.pop()
        snake.coordinates.pop()
    # Check collisions
    if check_collisions(snake):
        game_over()
    else:
        after_job = window.after(SPEED, next_turn, snake, food)

def change_direction(new_dir):
    global direction
    opposites = {'left':'right','right':'left','up':'down','down':'up'}
    if new_dir != opposites.get(direction):
        direction = new_dir

def check_collisions(snake):
    x, y = snake.coordinates[0]
    # Wall collision
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    # Self collision
    return (x, y) in snake.coordinates[1:]

def game_over():
    global game_over_sound, after_job
    # Cancel any pending loop call
    if after_job:
        window.after_cancel(after_job)
    # Play game-over sound asynchronously (non-blocking)
    game_over_sound = playsound("./assets/gameover.mp3", block=False)
    # Show "GAME OVER" text
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2.5,
                       font=('consolas', 40), text="GAME OVER", fill="red", tag="gameover")
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 1.5,
                       font=('consolas', 20), text="press 'ENTER' button to restart", fill="white", tag="gameover")

def start_game(event=None):
    global direction, score, after_job, game_over_sound
    # Stop any playing sound
    if game_over_sound and game_over_sound.is_alive():
        game_over_sound.stop()
    # Cancel pending loop (if any)
    if after_job:
        window.after_cancel(after_job)
    # Reset game state
    direction = 'down'
    score = 0
    score_label.config(text=f"Score: {score}")
    canvas.delete("all")
    # Create new snake and food
    snake = Snake()
    food = Food()
    next_turn(snake, food)

# --- Key bindings ---
window.bind("<Left>",  lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))
window.bind("<Up>",    lambda e: change_direction("up"))
window.bind("<Down>",  lambda e: change_direction("down"))
# Press Enter to restart the game
window.bind("<Return>", start_game)

# Start the first game
start_game()

window.mainloop()
