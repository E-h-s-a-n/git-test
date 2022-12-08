from pprint import pprint

data = open('./day_08.txt').read().strip()
lines = data.split('\n')

ver = len(lines)
hor = len(lines[0])

i = 5
for i in range(0, hor):
    tree = lines[0][i]
    left = (x for x in lines[0][0:i])
    right = (x for x in lines[0][i+1:])
    for i in left:
        print(i, end='')
    print(f' {tree}')
    # print(''.join(left) ,tree, ''.join(right))
    

def part1():
    visible_count = 0
    for i in range(1, ver-1):
        for j in range(1, hor-1):
            tree = int(lines[i][j])
            if tree==0: continue
            if tree==1:
                tree = 10
            # 3 2 1 0
            visibility = 4

            try:
                up = int(''.join(lines[x][j] for x in range(0, i)), base=tree)
                if tree==10 and up!=0: raise ValueError
                # print('visible')
            except ValueError:
                visibility -= 1

            try:
                down = int(''.join(lines[x][j] for x in range(i+1, ver)), base=tree)
                if tree==10 and down!=0: raise ValueError
                # print('visible')
            except ValueError:
                visibility -= 1

            try:
                left = int(lines[i][0:j], base=tree)
                if tree==10 and left!=0: raise ValueError
                # print('visible')
            except ValueError:
                visibility -= 1

            try:
                right = int(lines[i][j+1:], base=tree)
                if tree==10 and right!=0: raise ValueError
                # print('visible')
            except ValueError:
                visibility -= 1

            if visibility>0:
                visible_count += 1

        # print(visible_count)
        # break

    print(visible_count+ 99+ 99+ 97+ 97) #1662