from sys import stdin
import re

answer = 0
regex_pattern = r"(\D\D\D):(.*)"
field_set = set()
better_correct = True

for line in [line.rstrip() for line in stdin.readlines()]:
    if (line == ''):
        print('cont')
        if ((len(field_set) == 7 and 'cid' not in field_set) or len(field_set) == 8):
            answer += 1
        field_set = set()
        continue

    correct = True
    fields = line.split(' ')
    
    for field in fields:
        match = re.match(regex_pattern, field).group
        code = match(1)
        value = match(2)

        if code == 'byr':
            if int(value) >= 1920 and int(value) <= 2002:
                field_set.add(code)
        elif code == 'iyr':
            if int(value) >= 2010 and int(value) <= 2020:
                field_set.add(code)
        elif code == 'eyr':
            if int(value) >= 2020 and int(value) <= 2030:
                field_set.add(code)
        elif code == 'hgt':
            new_regex = r'(\d+)(.*)'
            match = re.match(new_regex, value).group

            number = int(match(1))
            metric = match(2)

            if number >= 150 and number <= 193 and metric == 'cm':
                field_set.add(code)
            elif number >= 59 and number <= 76 and metric == 'in':
                field_set.add(code)

        elif code == 'hcl':
            if re.match(r'#([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])', value):
                field_set.add(code)

        elif code == 'ecl':
            color_set = { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }
            
            if value in color_set:
                field_set.add(code)

        elif code == 'pid':
            if len(value) == 9:
                field_set.add(code)

print(answer)



