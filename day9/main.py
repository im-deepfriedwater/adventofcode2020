import re
from sys import stdin

answer = None

window = []
target = -1
numbers = [int(line.rstrip()) for line in stdin.readlines()]

for i, line in enumerate(numbers):
    num = int(line)
    if len(window) == 25:
        sum_found = False
        for number in window:
            if num - number in window:
                sum_found = True
                break
        if not sum_found:
            target = num
            break
        window.pop(0)
    window.append(num)


for i, number in enumerate(numbers):
    sum = 0
    found = False
    answer_list = []


    for inner_number in numbers[(i):]:
        answer_list.append(inner_number)
        sum += inner_number

        if sum > target:
            break

        if sum == target:
            found = True

    if found:
        print(min(answer_list) + max(answer_list))
        break
            
