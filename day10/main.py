from sys import stdin

difference = {}
difference[1] = 1
difference[2] = 0
difference[3] = 1
numbers = set()

minimum = 9999999999999999999
maximum = -1

for jolt in [line.rstrip() for line in stdin.readlines()]:
    if jolt == '':
        break

    jolt_number = int(jolt)
    minimum = min(minimum, jolt_number)
    maximum = max(maximum, jolt_number)
    numbers.add(jolt_number)

memoized = {}

# sort of part 1, messed it up trying to write part 2
# def recurse(minimum, maximum, current, numbers, difference, difference_value):
#     if current not in numbers:
#         return False
#     elif current == maximum:
#         return True

#     for i in [1, 2, 3]:
#         if recurse(minimum, maximum, current + i, numbers, difference, i):
#             difference[i] += 1
#             return True

# if recurse(minimum, maximum, minimum, numbers, difference, 0):
#     print(difference[1] * difference[3])


numbers.add(0)
numbers.add(maximum + 3)

def memoize(function):
    cache = {}

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = function(*args)
        cache[args] = result

        return result
    return memoized_func

@memoize
def recurse_christmas(start, maximum):
    global numbers

    sum = 0

    if start not in numbers:
        return 0

    if start == maximum:
        return 1
    
    for i in [1,2,3]:
        sum += recurse_christmas(start + i, maximum)

    return sum


print(recurse_christmas(0, maximum + 3))