from sys import stdin

tree_map = [line.rstrip() for line in stdin.readlines()]
end_of_map = len(tree_map) - 1
width_of_map = len(tree_map[0])



def calculate_tree_impacts(slope_x, slope_y):
    global tree_map
    global end_of_map
    global width_of_map

    current_x, current_y = 0, 0
    trees_encountered = 0 

    while True:
        current_x += slope_x
        current_y += slope_y

        if current_y > end_of_map:
            break

        if current_x >= width_of_map:
            print(current_x, current_x - width_of_map)
            current_x = current_x - (width_of_map)
        try: 
            if tree_map[current_y][current_x] == '#':
                trees_encountered += 1 
        except IndexError:
            print('error', current_x, current_y, end_of_map)
            break
        
    return trees_encountered
        
print(calculate_tree_impacts(1, 1), calculate_tree_impacts(3, 1), calculate_tree_impacts(5, 1), calculate_tree_impacts(7, 1), calculate_tree_impacts(1, 2))
print(calculate_tree_impacts(1, 1) * calculate_tree_impacts(3, 1) * calculate_tree_impacts(5, 1) * calculate_tree_impacts(7, 1) * calculate_tree_impacts(1, 2))