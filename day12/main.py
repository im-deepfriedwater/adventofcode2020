import math
from sys import stdin

answer = None
commands = []

for line in [line.rstrip() for line in stdin.readlines()]:
    if line == '':
        continue

    command, value = line[0], int(line[1:])
    commands.append((command, value))

# returns n,s,e,w
def move_in_direction(direction, value, current_position):
    new_position = current_position

    if direction == 'N':
        new_position[1] += value
    elif direction == 'S':
        new_position[1] -= value
    elif direction == 'E':
        new_position[0] += value
    elif direction == 'W':
        new_position[0] -= value

    return new_position

# returns current degrees
def turn_ship(direction, degrees, current_degree):
    current = current_degree

    if direction == 'R':
        current += degrees
        if current > 359:
            current %= 360
    elif direction == 'L':
        current -= degrees
        if current < -359:
            current %= -360

    if current < 0:
        current += 360
    return current

def move_forward(direction, value, current_position):
    new_position = current_position

    if direction == 0:
        new_position[1] += value
    elif direction == 90:
        new_position[0] += value
    elif direction == 180:
        new_position[1] -= value
    elif direction == 270:
        new_position[0] -= value

    return new_position

current_direction = 90
current_position = [0, 0]

for command, value in commands:
    if command in ['N', 'S', 'E', 'W']:
        current_position = move_in_direction(command, value, current_position)
    elif command in ['L', 'R']:
        current_direction = turn_ship(command, value, current_direction)
    elif command == 'F':
        current_position = move_forward(current_direction, value, current_position)
    
print(current_position, current_direction)
print(abs(current_position[0]) + abs(current_position[1]))

# 2532 not the answer
# 3403 too high
# 998 is answer








