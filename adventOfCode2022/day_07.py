from pprint import pprint

data = open('./day_07.txt').read().strip()
lines = data.split('\n')

line_number = 1
dir_size = {}
current_path = []
for line in lines:
    # words = line.split()
    
    if line.startswith('$ cd'):
        current_dir = line.split(' ')[-1]
        
        if current_dir == '..': 
            current_path.pop(); 
        else: 
            # possible duplicate directory name in different paths
            if dir_size.get(current_dir):
                current_dir = current_dir + f'{+line_number}'
            
            current_path += [current_dir]
        # TODO: replace with default dict
        dir_size[current_dir] = 0

    elif not(line.startswith('$') or line.startswith('dir')):
        size = int(line.split(' ')[0])
        for path in current_path:
            dir_size[path] += size
    line_number += 1

del dir_size['..']
part1_result = 0

needed_storage =  30_000_000 - (70_000_000 - dir_size['/'])
part2_min = dir_size['/']
pprint(dir_size)

for k,v in dir_size.items():
    if v < part2_min and v >= needed_storage:
        part2_min = v
    
    if v <= 100000:
        part1_result += v

print(part1_result, part2_min)
# sorted_size = sorted(dir_size.items(), key=lambda i: i[1])

'''
current_dir = ''
for l in lines:
    if l.startswith('$ cd'):
        current_dir = l.split(' ')[-1]
        # if name == '..': continue
        # dir_size[current_dir] = 0
        continue
    
    if l.startswith('dir'):
        dir_name = l.split(' ')[-1]
        dir_size[current_dir] += int(dir_size[dir_name])

with open('my_file.txt', 'w') as f:
    pprint(dir_size, f)

result_sum = 0
for k,v in dir_size.items():
    if v <= 100000:
        print(k,v)
        result_sum += v

print(result_sum)
'''