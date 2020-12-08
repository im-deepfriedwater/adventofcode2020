import re
from sys import stdin

class Operation:
    def __init__(self, command, value):
        self.command = command
        self.value = value

visited_set = set()
commands = []

regex = r'(nop|acc|jmp) ([+-]\d+)'

for line in [line.rstrip() for line in stdin.readlines()]:
    if line == '':
        continue
    matches = re.match(regex, line).group
    command = matches(1)
    value = int(matches(2))
    commands.append(Operation(command, value))

nop_indices = [i for i, x in enumerate(commands) if x.command == 'nop']
jmp_indices = [i for i, x in enumerate(commands) if x.command == 'jmp']

def test_for_infinite(indices, new_swap, commands):
    for swap_index in indices:
        accumlator = 0
        current_command = commands[0]
        current_index = 0
        visited_set = set()
        print(swap_index, 'swap index baybeeeee', new_swap)
        while current_command not in visited_set:
            if swap_index == current_index:
                new_command = new_swap
            else:
                new_command = commands[current_index].command
        
            if new_command == 'jmp':
                current_index += current_command.value
            elif new_command == 'acc':
                accumlator += current_command.value
                current_index += 1
            else:
                current_index += 1
            
            visited_set.add(current_command)

            if current_index == len(commands):
                print(accumlator)
                return
            
            current_command = commands[current_index]

test_for_infinite(nop_indices, 'jmp', commands)
test_for_infinite(jmp_indices, 'nop', commands)