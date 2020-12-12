from sys import stdin

answer = None

seat_chart = []
for line in [line.rstrip() for line in stdin.readlines()]:
    if line == '':
        break

    seat_chart.append(list(line))

def is_in_bounds(x, y, seat_chart):
    return x >= 0 and x < len(seat_chart[0]) and y >= 0 and y < len(seat_chart)

def has_no_occupied_adjacents(x, y, seat_chart):
    result = True

    for delta in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        x_to_check, y_to_check = delta[0] + x, delta[1] + y 

        if is_in_bounds(x_to_check, y_to_check, seat_chart) and seat_chart[y_to_check][x_to_check] == '#':
            result = False
            break

    return result

def has_four_or_more_adjacents(x, y, seat_chart):
    adjacents_count = 0

    for delta in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        x_to_check, y_to_check = delta[0] + x, delta[1] + y 

        if is_in_bounds(x_to_check, y_to_check, seat_chart) and seat_chart[y_to_check][x_to_check] == '#':
            adjacents_count += 1

    return adjacents_count >= 4

def has_no_occupied_adjacent_visibles(x, y, seat_chart):
    result = True

    for delta in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        x_to_check, y_to_check = delta[0] + x, delta[1] + y 
        result = True

        while is_in_bounds(x_to_check, y_to_check, seat_chart):
            if seat_chart[y_to_check][x_to_check] == '#':
                result = False
                break

            if seat_chart[y_to_check][x_to_check] == 'L':
                result = True
                break

            x_to_check += delta[0]
            y_to_check += delta[1]
        
        if not result:
            break

    return result

def has_five_or_more_adjacent_visibles(x, y, seat_chart):
    adjacents_count = 0

    for delta in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        x_to_check, y_to_check = delta[0] + x, delta[1] + y 

        while is_in_bounds(x_to_check, y_to_check, seat_chart):
            if seat_chart[y_to_check][x_to_check] == '#':
                adjacents_count += 1
                break

            if seat_chart[y_to_check][x_to_check] == 'L':
                break
            
            x_to_check += delta[0]
            y_to_check += delta[1]
        
        if adjacents_count >= 5:
            break


    return adjacents_count >= 5

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

state_changed = True

while state_changed:
    state_changed = False
    changes = []

    for y, row in enumerate(seat_chart):
        for x, seat in enumerate(row):
            if seat == 'L':
                if has_no_occupied_adjacent_visibles(x, y, seat_chart):
                    changes.append((y, x, '#'))
                    state_changed = True

            if seat == '#':
                if has_five_or_more_adjacent_visibles(x, y, seat_chart):
                    changes.append((y, x, 'L'))
                    state_changed = True

    for change in changes:
        seat_chart[change[0]][change[1]] = change[2]

answer_part_one = 0

for row in seat_chart:
    for seat in row:
        if seat == '#':
            answer_part_one += 1



print(answer_part_one)
