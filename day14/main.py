import re
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

for program in programs:
    for instruction in program['instructions']:
        string = list(format(int(instruction['value']), '036b'))
        for i, mask_value in enumerate(program['mask']):
            string[i] = mask_value if mask_value != 'X' else string[i]
        memory[instruction['address']] = int(''.join(string), 2)


