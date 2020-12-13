from sys import stdin
from functools import reduce
import math
# part 1
# mins waiting * id of bus

earliest_time, ids = [line.rstrip() for line in stdin.readlines()]
earliest_time = int(earliest_time)
buses = [int(id) for id in ids.split(',') if id != 'x']

# bus id, waiting time
earliest_waiting_time = 999999999999
earliest_bus = -1

for bus in buses:
    q, r = divmod(earliest_time, bus)

    multiplier = q if q * bus > earliest_time else q + 1
    if (bus * multiplier) - earliest_time < earliest_waiting_time:
        earliest_waiting_time = (bus * multiplier) - earliest_time
        earliest_bus = bus

# print(earliest_waiting_time * earliest_bus)
# helpful hints from reddit I needed to solve this 

#    /*
#         ** Example:
#         **
#         ** Previous bus is 7, this bus is 13, with delay +1.
#         ** A time T is needed such that:
#         **      7x == T
#         **     13y == (T + 1)
#         **
#         ** Performing an iterative search for T on multiples of 7 and checking (T + 1)
#         ** eventually reveals that:
#         **   (7 * 11) == 77
#         **   (13 * 6) == 78
#         **
#         ** To find further times that match this condition, imagine some value W added to T.
#         **    7j == T + W
#         **   13k == (T + 1) + W

# ** Substituting:
# **    7j == 7x + W,  and j == x + (W / 7)
# **   13k == 13y + W, and k == y + (W / 13)
# ** For j and k to be integers, since x and y are integers, W must be a multiple of both 7 and 13.
# ** Since all input numbers are conveniently prime, the smallest multiple of both 7 and 13 is (7 * 13).
# ** Thus, W == (7 * 13) == 91.
# **
# **
# ** Next, a time T is needed such that:
# **      7x == T
# **     13y == (T + 1)
# **     59z == (T + 4)
# **
# ** Performing an iterative search from 77, adding multiples of 91, eventually reveals that:
# **    (7 * 50) == 350
# **   (13 * 27) == 351
# **    (59 * 6) == 354
# **
# ** As above, the next T that matches this condition would be 350 + (7 * 13 * 59) == 350 + (5369) == 5719.
# */!<

# accumulate the LCM of the buses you have seen so far, and brute force the multiple of that LCM that satisfies the next bus. 
buses =  [(i, int(id)) for i, id in enumerate(ids.split(',')) if id != 'x']

# bus id, waiting time
earliest_time_stamp = 0
number_found = False
multiplier = buses[0]
seen_buses = []
incrementer = buses[0][1]

for i in range(0, len(buses)):
    if i > 1:
        incrementer = reduce(lambda a, b: a * b[1], seen_buses, 1)
    seen_buses.append(buses[i])
    found = False

    while not found:
        print('while', buses[i])
        found = True
        for seen_bus in seen_buses:
            print(earliest_time_stamp, seen_bus[1], seen_bus, incrementer, seen_buses)
            if (earliest_time_stamp + seen_bus[0]) % seen_bus[1] != 0:
                found = False
                break
        if not found:    
            earliest_time_stamp += incrementer



print(earliest_time_stamp)


   