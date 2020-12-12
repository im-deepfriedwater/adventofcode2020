from sys import stdin

answer = None

seat_chart = []
for line in [line.rstrip() for line in stdin.readlines()]:
    if line == '':
        break

    seat_chart.append(list(line))


def has_no_occupied_adjacents(x, y, seat_chart):
    has_no_left = x != 0 and seat_chart[y][x-1] == 'L'
    has_no_right = x <= len(seat_chart[0]) - 2 and seat_chart[y][x + 1] == 'L'
    has_no_up = y != 0 and seat_chart[y-1][x] == 'L'
    has_no_down = y <= len(seat_chart) - 2 and seat_chart[y+1][x] == 'L'

    has_no_up_left = x != 0 and y != 0 and seat_chart[y - 1][x - 1] == 'L'
    has_no_up_right = x <= len(seat_chart[0]) - 2 and y != 0 and seat_chart[y - 1][x + 1] == 'L'
    has_no_down_left = x != 0 and y <= len(seat_chart) - 2 and seat_chart[y + 1][x - 1] == 'L'
    has_no_down_right = x <= len(seat_chart[0]) - 2 and y <= len(seat_chart) - 2 and seat_chart[y + 1][x + 1] == 'L'

    return has_no_left and has_no_right and has_no_up and has_no_down and has_no_up_left and has_no_up_right and has_no_down_left and has_no_down_right

def has_four_or_more_adjacents(x, y, seat_chart):
    count = 0

    has_no_left = x > 0 and seat_chart[y][x - 1] == '#'
    has_no_right = x != len(seat_chart[0]) - 1 and seat_chart[y][x + 1] == '#'
    has_no_up = y != 0 and seat_chart[y-1][x] == '#'
    has_no_down = y <= len(seat_chart) and seat_chart[y+1][x] == '#'

    has_no_up_left = x != 0 and y != 0 and seat_chart[y - 1][x - 1] == '#'
    has_no_up_right = x <= len(seat_chart[0]) - 2 and y != 0 and seat_chart[y - 1][x + 1] == '#'
    has_no_down_left = x != 0 and y <= len(seat_chart) - 2 and seat_chart[y + 1][x - 1] == '#'
    has_no_down_right = x <= len(seat_chart[0]) - 2 and y <= len(seat_chart) - 2 and seat_chart[y + 1][x + 1] == '#'

    for check in [has_no_left, has_no_right, has_no_up, has_no_down, has_no_up_left, has_no_up_right, has_no_down_left, has_no_down_right]:
        count += 1 if check else 0

    return count >= 4

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

state_changed = True
answer_part_one = -1

while state_changed:
    state_changed = False
    changes = []

    for y, row in enumerate(seat_chart):
        for x, seat in enumerate(row):
            if seat == 'L':
                if has_no_occupied_adjacents(x, y, seat_chart):
                    changes.append((y, x, '#'))
                    state_changed = True

            if seat == '#':
                if has_four_or_more_adjacents(x, y, seat_chart):
                    changes.append((y, x, 'L'))
                    state_changed = True

    if state_changed:
        answer_part_one += 1

    for change in changes:
        seat_chart[change[0]][change[1]] = change[2]

print(seat_chart)
print(answer_part_one)