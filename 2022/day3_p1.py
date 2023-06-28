import string

f = '2022/day3.txt'
list_items = open(f, 'r')

sum_priorities = 0

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
shared_list = []


for line in list_items:
    size_compartiment = len(line)//2
    first_compartiment = line[int(size_compartiment):]
    second_compartiment = line[:int(size_compartiment)]

    for i in range(size_compartiment):
        for j in range(size_compartiment):
            if first_compartiment[i] == second_compartiment[j]:
               shared_item = first_compartiment[i]

    shared_list.append(shared_item)
list_items.close()

for i in range(len(shared_list)):
    if shared_list[i].islower():
        for j in range(26):
            if shared_list[i] == lowercase_alphabet[j]:
                sum_priorities += j + 1
    else:
        for j in range(26):
            if shared_list[i] == uppercase_alphabet[j]:
                sum_priorities += j + 27

print(shared_list)
print(sum_priorities)