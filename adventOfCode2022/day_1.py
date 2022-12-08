
with open('day1_input', 'r') as calories:
    # print(calories)
    elf_total_calorie = []
    calorie_sum = 0
    for calorie in calories:
        if c:= calorie.strip():
            calorie_sum += int(c)
        else:
            elf_total_calorie += [calorie_sum]
            calorie_sum = 0

print(max(elf_total_calorie))

elf_total_calorie.sort(reverse=True)

print(sum(elf_total_calorie[0:3]))


