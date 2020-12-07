import re
from sys import stdin

# dotted blue bags contain 3 wavy bronze bags, 5 clear tomato bags.

class Node:
    def __init__(self, value, node_type):
        self.children = []
        self.value = value
        self.node_type = node_type

    def add(self, new_child):
        self.children.append(new_child)
    
    def recurse_for_gold_bag(self, visited, is_parent):
        if self in visited:
            return False
        else:
            visited.add(self)
        
        if 'shiny gold' in self.node_type and not is_parent:
            return True

        for child in self.children:
            # print('child', child.node_type)
            if child.recurse_for_gold_bag(visited, False):
                return True
        
        return False
    
answer = 0

container_pattern = r'([a-z]+ [a-z]+).'
child_pattern = r'(\d) (\D+ \D+) [bag|bags]\.*'

unique_bags = set()
bags = {}

for line in [line.rstrip() for line in stdin.readlines()]:

    node_type = re.match(container_pattern, line).groups(1)[0]

    if node_type in bags:
        current_node = bags[node_type]
    else:
        current_node = Node(None, node_type)
        bags[node_type] = current_node
        unique_bags.add(current_node)

    child_bags = line.split('contain ')[1].split(',')

    print(len(child_bags), line)

    if 'no other bags.' in line:
        continue

    for child_bag in child_bags:
        child_bag = child_bag.strip()
        child_node_match_groups = re.match(child_pattern, child_bag).groups
        child_node_value = child_node_match_groups(1)[0]
        child_node_type = child_node_match_groups(2)[1]

        if child_node_type in bags:
            current_node.add(bags[child_node_type])
        else:
            new_bag = Node(child_node_value, child_node_type)
            current_node.add(new_bag)
            unique_bags.add(new_bag)
            bags[child_node_type] = new_bag

for bag in unique_bags:
    visited = set()
    
    if bag.recurse_for_gold_bag(visited, True):
        answer += 1
    
print(answer)

# not 6
# not 33
# answer was 337