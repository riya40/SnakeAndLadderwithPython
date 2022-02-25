import random
"""Welcome To  Snake and Ladder game
Initiating the values for snake ,ladder,and winpoint
Initiating the methods for Snake and Ladder"""

LADDER = {
    10: 31,
    20: 42,
    45: 78,
    70: 98
}

SNAKE = {
    30: 2,
    50: 21,
    68: 46,
    72: 55,
    89: 72
}

WIN_POINT = 100


def check_snake(prev_pos, dice):
    new_pos = prev_pos + dice
    if new_pos <= WIN_POINT:
        _snake = SNAKE.get(new_pos)
        if _snake:
            print("snake appered", _snake)
            return _snake
        else:
            return new_pos

    return prev_pos


