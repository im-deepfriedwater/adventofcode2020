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

def turn_waypoint(direction, degrees, waypoint_position):
    new_position = waypoint_position

    if degrees == 90 and direction == 'R':
        new_position = [new_position[1], -new_position[0]]
    elif degrees == 90 and direction == 'L':
        new_position = [-new_position[1], new_position[0]]
    elif degrees == 180:
        new_position = [-new_position[0], -new_position[1]]
    if degrees == 270 and direction == 'R':
        new_position = [-new_position[1], new_position[0]]
    elif degrees == 270 and direction == 'L':
        new_position = [new_position[1], -new_position[0]]

    return new_position

def move_forward(value, current_position, ship_position):
    new_position = ship_position

    for _ in range(value):
        new_position[0] += current_position[0]
        new_position[1] += current_position[1]

    return new_position

current_position = [10, 1]
ship_position = [0, 0]

for command, value in commands:
    if command in ['N', 'S', 'E', 'W']:
        current_position = move_in_direction(command, value, current_position)
    elif command in ['L', 'R']:
        current_position = turn_waypoint(command, value, current_position)
    elif command == 'F':
        ship_position = move_forward(value, current_position, ship_position)
    

print(current_position)
print(abs(ship_position[0]) + abs(ship_position[1]))

# 2532 not the answer
# 3403 too high
# 998 is answer

# 10, 10
# R90

# 112266 too high