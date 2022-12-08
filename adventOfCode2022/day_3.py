from string import ascii_letters
priority =  dict(zip(ascii_letters,range(1, len(ascii_letters)+1)))

rucksacks_contents = [line.strip() for line in open("aoc2022/day3.txt")]

total_sum = 0

# --------- PART TWO ---------
for i in range(0,len(rucksacks_contents),3):
    elf_group = [rucksacks_contents[j] for j in range(i, i+3)]
    common_type = set.intersection(*map(set, elf_group))
    total_sum += priority[common_type.pop()]

print(total_sum)




# --------- PART ONE ---------
# for items in rucksacks_contents:
#     first_part = items[0:len(items)//2]
#     second_part = items[len(items)//2:]

#     for i in first_part:
#         if i in second_part:
#             print(i)
#             total_sum += priority[i]
#             break
# print(total_sum)

