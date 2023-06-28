import string

f = '2022/day3.txt'
list_items = open(f, 'r')

sum_priorities = 0
badge_item = 0
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
badge_list = []
group_elves = []

for line in list_items:
    line = line.rstrip()
    if len(group_elves) == 2:
        group_elves.append(line)
        size_first = len(group_elves[0])
        size_second = len(group_elves[1])
        size_thrid = len(group_elves[2])

        for i in range(size_first):
            for j in range(size_second):
                for k in range(size_thrid):
                   if group_elves[0][i] == group_elves[1][j] == group_elves[2][k]:
                       badge_item = group_elves[2][k] 

        badge_list.append(badge_item)
        group_elves.clear()
    else:
        group_elves.append(line)
list_items.close()

for i in range(len(badge_list)):
    if badge_list[i].islower():
        for j in range(26):
            if badge_list[i] == lowercase_alphabet[j]:
                sum_priorities += j + 1
    else:
        for j in range(26):
            if badge_list[i] == uppercase_alphabet[j]:
                sum_priorities += j + 27

print(len(badge_list))
print(sum_priorities)