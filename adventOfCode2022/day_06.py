import sys
print(sys.argv[-1])

data = open('day_06.txt').read().strip()
# data = (x for x in open('day_06.txt').read().strip())
# chars = [x for x in data]
part_one, part_two = 4, 14
part_1 = False
part_2 = False

def printAnswer():
    for i in range(0, len(data)-part+1):
        x = set(data[i:i+part])
        if len(x)>=part:
            print(i+part)
            break

    # we can do the two part in one loop too 

part = part_one
printAnswer()
part = part_two
printAnswer()