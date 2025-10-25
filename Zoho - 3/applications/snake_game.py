import random
import os

# Game configuration
width = 10
height = 10

# Initial snake setup
snake = [(5, 5)]
direction = 'r'  # Initial direction
food = ()

def place_food():
    while True:
        new_food = (random.randint(0, height - 1), random.randint(0, width - 1))
        if new_food not in snake:
            return new_food

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(height):
        for j in range(width):
            if (i, j) == snake[0]:
                print('O', end=' ')  # Snake's head
            elif (i, j) in snake:
                print('o', end=' ')  # Snake's body
            elif (i, j) == food:
                print('X', end=' ')  # Food
            else:
                print('.', end=' ')  # Empty space
        print()
    print(f"Snake Length: {len(snake)}")

def move_snake(direction):
    head = snake[0]
    if direction == 'r':
        new_head = (head[0], (head[1] + 1) % width)
    elif direction == 'l':
        new_head = (head[0], (head[1] - 1 + width) % width)
    elif direction == 'u':
        new_head = ((head[0] - 1 + height) % height, head[1])
    elif direction == 'd':
        new_head = ((head[0] + 1) % height, head[1])
    else:
        return False

    if new_head in snake:
        return False  # Snake bites itself — game over

    snake.insert(0, new_head)

    if new_head == food:
        return True  # Snake grows
    else:
        snake.pop()  # Move forward (no growth)
        return True

# Place the first food
food = place_food()

# Game loop
while True:
    print_board()
    move = input("Move (r/l/u/d): ").strip().lower()
    if move not in ['r', 'l', 'u', 'd']:
        print("Invalid move! Use r/l/u/d only.")
        continue

    direction = move
    result = move_snake(direction)

    if result is False:
        print_board()
        print("Game Over! The snake bit itself.")
        break

    if snake[0] == food:
        food = place_food()