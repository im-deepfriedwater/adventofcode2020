from sys import stdin
import re

regex_pattern = r"(\d+)-(\d+) (\D): (.*)"

answer_1 = 0
answer_2 = 0

for line in [line.rstrip() for line in stdin.readlines()]:

    # Part 1 variables
    match = re.match(regex_pattern, line).group
    lower_bound, upper_bound, target_letter, search_string = int(match(1)), int(match(2)), match(3), match(4)
    valid_password_1 = True
    valid_password_2 = False
    current_target_letter_count = 0

    # Part 2 variables
    has_first_character, has_second_character = False, False
    first_index, second_index = lower_bound - 1, upper_bound - 1

    for index, character in enumerate(search_string):
        if character == target_letter:
            current_target_letter_count += 1

        if not has_first_character and first_index == index and character == target_letter:
            has_first_character = True

        if not has_second_character and second_index == index and character == target_letter:
            has_second_character = True
    
    if current_target_letter_count >= lower_bound and current_target_letter_count <= upper_bound:
        answer_1 += 1
        valid_password_1 = False

    if has_first_character != has_second_character and (has_first_character or has_second_character):
        answer_2 += 1
        valid_password_2 = True

    print(lower_bound, upper_bound, target_letter, search_string, valid_password_1, valid_password_2)


print(answer_1, answer_2)


           
