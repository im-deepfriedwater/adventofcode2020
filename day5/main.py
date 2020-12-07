from sys import stdin

highest_identification = -1
number_set = set()

for line in [line.rstrip() for line in stdin.readlines()]:
    row = int(line[:7].replace('F','0').replace('B', '1'), 2)
    column = int(line[7:10].replace('R', '1').replace('L', '0'), 2)
    identification = (row * 8) + column
    highest_identification = max(highest_identification, identification)
    number_set.add(identification)
print(highest_identification)


for number in range(1, highest_identification):
    if number not in number_set:
        if number + 1 in number_set and number - 1 in number_set:
            print(number)
            break;