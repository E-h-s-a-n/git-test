from pprint import pprint

data = open('./day_08.txt').read().strip()
lines = data.split('\n')

ver = len(lines)
hor = len(lines[0])

# for PART 2
for i in range(1, ver-1):
    distance_multiply = 1
    for j in range(1, hor-1):
        tree = int(lines[i][j])

        distance_left = j
        for x in range(j-1, 0, -1):
            if int(lines[i][x]) >= tree:
                distance_left = j - x
                break

        distance_right = hor - j - 1
        for x in range(j+1, hor):
            if int(lines[i][x]) >= tree:
                distance_right = x - j
                break
        # print(i+1, j+1, tree, distance_right)
        distance_multiply = max(
            distance_multiply, distance_left*distance_right)
        # print(i+1, j+1, tree, distance_right*distance_left, distance_multiply)

    break


def part1():
    visible_count = 0
    for i in range(1, ver-1):
        for j in range(1, hor-1):
            tree = int(lines[i][j])
            if tree == 0:
                continue
            if tree == 1:
                tree = 10


            try:
                left = int(lines[i][0:j], base=tree)
                if tree == 10 and left != 0:
                    raise ValueError
                # print('visible')
                visible_count += 1
                continue
            except ValueError:
                pass

            try:
                right = int(lines[i][j+1:], base=tree)
                if tree == 10 and right != 0:
                    raise ValueError
                # print('visible')
                visible_count += 1
                continue
            except ValueError:
                pass

            try:
                up = int(''.join(lines[x][j] for x in range(0, i)), base=tree)
                if tree == 10 and up != 0:
                    raise ValueError
                # print('visible')
                visible_count += 1
                continue
            except ValueError:
                pass

            try:
                down = int(''.join(lines[x][j] for x in range(i+1, ver)), base=tree)
                if tree == 10 and down != 0:
                    raise ValueError
                # print('visible')
                visible_count += 1
                continue
            except ValueError:
                pass
            


    print(visible_count + 99 + 99 + 97 + 97)  # 1662


part1()
