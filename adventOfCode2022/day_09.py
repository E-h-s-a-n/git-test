from pprint import pprint, pp
data = open('day_09.txt').read().strip()
lines = data.split('\n')

head = {'x': 0, 'y': 0}
# tail = {'x': 0, 'y': 0}
tails = []
tailed = set()

DIR = {'U': 'y', 'D': 'y',
       'L': 'x', 'R': 'x'}
UNIT = {'U': 1, 'D': -1,
        'L': -1, 'R': 1}

# CODE = {'U': (0, 1), 'D': (0, -1),
#         'R': (1, 0), 'L': (-1, 0)}

for i in range(9):
    tails.append({'x': 0, 'y': 0})

for line in lines:
    aim, move, unit = DIR[line[0]], int(line[1:]), UNIT[line[0]]
    
    for m in range(move):
        head[aim] += 1 * unit
        temp_head = head
        for x in range(len(tails)):
            tail = tails[x]
            if tail['y'] == temp_head['y']:
                if abs(tail['x'] - temp_head['x']) > 1:
                    tail['x'] += 1 * unit
            elif tail['x'] == temp_head['x']:
                if abs(tail['y'] - temp_head['y']) > 1:
                    tail['y'] += 1 * unit
            else:
                if abs(tail['x'] - temp_head['x']) > 1:
                    tail['x'] += 1 * unit
                    tail['y'] = temp_head['y']
                elif abs(tail['y'] - temp_head['y']) > 1:
                    tail['y'] += 1 * unit
                    tail['x'] = temp_head['x']
            temp_head = tails[x]
        
        tailed.add((tails[-1]['x'], tails[-1]['y']))
        
    # print(head)
    # pprint(tails)


print(len(tailed))
