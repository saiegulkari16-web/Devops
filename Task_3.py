# Snake game

import tkinter
import random

rows = 25
columns = 25
tile_size = 25

window_width = tile_size * columns
window_height = tile_size * rows

class tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title('Snake Game')
window.resizable(False, False) #To keep size fixed

canvas = tkinter.Canvas(window, bg = 'black', width = window_width, height = window_height, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#game
snake = tile(5*tile_size, 5*tile_size)#1 block
food = tile(10*tile_size, 10*tile_size)
snake_body = []# to increase the size
velocityX = 0
velocityY = 0
score = 0

game_over = False

def change_direction(e):
    global velocityX, velocityY, game_over
    if (game_over):
        return

    if(e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif(e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif(e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif(e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def move_snake():
    global snake, food, snake_body, game_over, score
    if(game_over):
        return
    
    if(snake.x < 0 or snake.x > window_width or snake.y < 0 or snake.y > window_height):
        game_over = True
        return
    print(f'score: {score}')
    
    for block in snake_body:
        if(snake.x == block.x and snake.y == block.y):
            game_over = True
            return

    #clash
    if(snake.x == food.x and snake.y == food.y):
        snake_body.append(tile(food.x, food.y))
        food.x = random.randint(0, columns-1) * tile_size
        food.y = random.randint(0, rows-1) * tile_size
        score += 1
    for i in range(len(snake_body)-1, -1, -1):
        if(i == 0):
            snake_body[i].x = snake.x
            snake_body[i].y = snake.y
        else:
            snake_body[i].x = snake_body[i-1].x
            snake_body[i].y = snake_body[i-1].y

    snake.x += velocityX * tile_size
    snake.y += velocityY * tile_size


def draw():
    global snake, food, snake_body, game_over, score

    move_snake()
    canvas.delete('all')

    #drawing food
    canvas.create_rectangle(food.x, food.y, food.x + tile_size, food.y + tile_size, fill = 'red')

    #drawing snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill = 'light green')

    #drawing snake body
    for block in snake_body:
        canvas.create_rectangle(block.x, block.y, block.x + tile_size, block.y + tile_size, fill = 'light green')

    if (game_over):
        canvas.create_text(window_width/2, window_height/2, font = 'Arial(heading)  60',text = f'Game Over: {score}', fill = 'cyan')
    else:
        canvas.create_text(30, 20, font = 'Arial(heading)  10',text = f'Score: {score}', fill = 'cyan')
    window.after(100, draw)

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()
