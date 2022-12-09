from pprint import pprint
data = open('day_09.txt').read().strip()
lines = data.split('\n')

head = {'x': 0, 'y': 0}
tail = {'x': 0, 'y': 0}
tailed = set()

DIR = {'U': 'y', 'D': 'y',
       'L': 'x', 'R': 'x'}
UNIT = {'U': 1, 'D': -1,
        'L': -1, 'R': 1}

CODE = {'U': (0, 1), 'D': (0, -1),
        'R': (1, 0), 'L': (-1, 0)}

class Tail():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

tails = []
for i in range(9):
    tails.append(Tail(0, 0))



# print(".... { head } ..... { tail } ....")
for line in lines:
    aim, move, unit = DIR[line[0]], int(line[1:]), UNIT[line[0]]
    # Up Down Left Right
    # print('---', line, '---')
    for m in range(move):
        head[aim] += 1 * unit

        if tail['y'] == head['y']:
            if abs(tail['x'] - head['x']) > 1:
                tail['x'] += 1 * unit
        elif tail['x'] == head['x']:
            if abs(tail['y'] - head['y']) > 1:
                tail['y'] += 1 * unit
        else:
            if abs(tail['x'] - head['x']) > 1:
                tail['x'] += 1 * unit
                tail['y'] = head['y']
            elif abs(tail['y'] - head['y']) > 1:
                tail['y'] += 1 * unit
                tail['x'] = head['x']

        tailed.add((tail['x'], tail['y']))
        # print(head, tail)

# tailed.add((0, 0)) 
print(len(tailed))
