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


def check_ladder(prev_point, dice_value):
    new_pos = prev_point + dice_value
    if new_pos <= WIN_POINT:
        _ladder = LADDER.get(new_pos)
        if _ladder:
            print("ladder appered", _ladder)
            return _ladder
        else:
            return new_pos
    return prev_point


def check_win(new_pos):
    return new_pos == WIN_POINT


def play(prev_pos):
    dice = throw_dice()
    is_snake = check_snake(prev_pos, dice)
    is_ladder = check_ladder(prev_pos, dice)
    if is_snake < prev_pos:  # if snake return snake value
        print("snake position appeared:", is_snake)
        return is_snake
    else:
        # if snake dont check for ledder / if ledder return ledder value
        if is_ladder > prev_pos:
            print("ladder position appeared:", is_ladder)
            return is_ladder
    i_won = check_win(is_ladder)  # if snake or ledder is there aviod win call
    if i_won:
        return -1
    else:
        return is_ladder


def throw_dice():
    return random.randint(1, 6)


player1 = 0
player2 = 0

while True:
    player1 = play(player1)
    if player1 == -1:
        print('player1! you won')
        break

    player2 = play(player2)
    if player2 == -1:
        print('player 2! you won')
        break
