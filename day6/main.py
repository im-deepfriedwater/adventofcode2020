from sys import stdin

answer = 0
alpha_dictionary = {}
group_size = 0

for line in [line.rstrip() for line in stdin.readlines()]:
    print(line)
    if line == '':
        print(alpha_dictionary)

        for character in alpha_dictionary:
            answer += 1 if alpha_dictionary[character] == group_size else 0
        alpha_dictionary = {}
        group_size = 0
        continue
    
    group_size += 1


    for character in line:
        if character not in alpha_dictionary:
            alpha_dictionary[character] = 1
        else:
            alpha_dictionary[character] += 1
        
for character in alpha_dictionary:
    answer += 1 if alpha_dictionary[character] == group_size else 0
    


print(answer)