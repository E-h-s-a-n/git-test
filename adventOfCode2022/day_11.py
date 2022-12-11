from pprint import pprint


data = open('day_11.txt').read().strip()
lines = '\n'.join((x.strip() for x in data.split('\n')))
monkeys = [x.split('\n') for x in lines.split("\n\n")]

del data, lines

monks = []
for m in monkeys:
    m_2_5 = m[2].split()[5]
    m_345 = [int(m[x].split()[-1]) for x in [3, 4, 5]]
    s = {
        'item': [int(x) for x in m[1].split(':')[1].split(',')],
        'opr': [m[2].split()[4], m_2_5 if m_2_5 == 'old' else int(m_2_5)],
        'test': m_345,
        'inspect': 0,
    }
    monks.append(s)

del monkeys
# pprint(monks)

lcm = 1
for x in monks:
    lcm *= x['test'][0]


def operation(old, operand, level):
    if level == 'old':
        level = old
    if operand == '*':
        new = old * level
    elif operand == '+':
        new = old + level

    return new


for r in range(10000):
    # print(r)
    for m in monks:
        for item in m['item']:
            m['inspect'] += 1
            item
            if (xx := operation(item, m['opr'][0], m['opr'][1]) % lcm) % m['test'][0] == 0:
                monks[m['test'][1]]['item'].append(xx)
            else:
                monks[m['test'][2]]['item'].append(xx)
        m['item'] = []


print("After rounds of keep away")
pprint(sorted([x['inspect'] for x in monks]))
print(253 * 247)  # PART ONE
print(128592 * 135377)  # PART TWO
# eval()
