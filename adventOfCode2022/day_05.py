data = open('day_05.txt').read().strip()
lines = [x for x in data.split('\n')]
gibberish = "\n".join(lines)
# moves[0] -> move 3 from 2 to 9
moves = gibberish.split('\n\n')[1].split('\n')
# print(moves[0].split(' '))
# ['move', '3', 'from', '2', 'to', '9']

stack1 = ['T', 'D', 'W', 'Z', 'V', 'P']
stack2 = ['L', 'S', 'W', 'V', 'F', 'J', 'D']
stack3 = ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H']
stack4 = ['R', 'S', 'J']
stack5 = ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W']
stack6 = ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B']
stack7 = ['V', 'J', 'P', 'C', 'B', 'D', 'N']
stack8 = ['P', 'T', 'B', 'Q']
stack9 = ['H', 'G', 'Z', 'R', 'C']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
# print(stacks)

for m in moves:
    m = m.split(' ')
    count, fromStack, toStack= int(m[1]), int(m[3])-1, int(m[5])-1

    # PART TWO
    stacks[toStack] += (i for i in stacks[fromStack][-count:])
    for x in range(count):
        stacks[fromStack].pop()

    '''for x in range(count):
        movingCrane = stacks[fromStack].pop()
        stacks[toStack].append(movingCrane)'''

print(''.join(x[-1] for x in stacks))