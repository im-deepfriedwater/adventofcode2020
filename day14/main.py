import re
import math
from functools import reduce
from sys import stdin

answer = None
programs = []
regex_mask = r"mask = ([1|0|X]+)"
regex_mem_instruction = r"mem\[([0-9]+)\] = ([0-9]+)"
program = None
memory = {}

for line in [line.rstrip() for line in stdin.readlines()]:
    if 'mask' in line:
        if program != None:
            programs.append(program)
        program = {}
        mask = re.match(regex_mask, line).group(1)
        program['mask'] = mask
        program['instructions'] = []
    else:
        match_group = re.match(regex_mem_instruction, line).group
        memory_address, value = match_group(1), match_group(2)
        program['instructions'].append({'address': memory_address, 'value': value})

programs.append(program)

def binary_convert(value):
    return format(int(value), f'036b')


def apply_mask(address, mask):
    padded_address = list(binary_convert(address))
    for i in range(len(padded_address)):
        if mask[i] == '1':
            padded_address[i] = mask[i]
    return ''.join(padded_address)

for program in programs:
    for instruction in program['instructions']:
        addresses = []
        initial_address = apply_mask(instruction['address'], program['mask'])
        floating_indices = [i for i, bit in enumerate(program['mask']) if bit == 'X']
        floating_indices = list(reversed(floating_indices))
        binary_counter_string = binary_convert(0)
        while int(binary_counter_string, 2) < math.pow(2, len(floating_indices)):
            new_address = list(initial_address)
            for i, floating_index in enumerate(floating_indices):
                new_address[floating_index] = binary_counter_string[len(binary_counter_string) - i - 1]
            addresses.append(int(''.join(new_address)))
            binary_counter_string = binary_convert(int(binary_counter_string, 2) + 1)

        for address in addresses:
            memory[address] = int(instruction['value'])

# 1350684480495 is too low
# 4712219970270 is too high ;-;

print(reduce(lambda a, b: a + memory[b], memory.keys(), 0))