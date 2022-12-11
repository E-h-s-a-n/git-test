from pprint import pprint

data = open('day_10.txt').read().strip()
lines = data.split('\n')

cycle = 0
x_register = 1
signals = []

crt_row = ""
sprite_pos = [x_register-1, x_register, x_register+1] #sprite has 3 pixels

def get_signal_strength(cycle_num, register_value):
    # PART ONE
    if (cycle_num-20) % 40 == 0:
        signals.append(cycle_num * register_value)
        return cycle_num * register_value
    return 'No signal'

def show_crt():
    # PART TWO
    global crt_row
    global sprite_pos

    index = len(crt_row)
    index -= (index // 40) * 40

    if index in sprite_pos:
        crt_row += '#'
    else:
        crt_row += '.'


for line in lines:
    command = line.split()[0]

    if command == 'noop':
        cycle += 1
        show_crt()
        # aa = get_signal_strength(cycle, x_register)
        continue
    
    if command == 'addx':
        cycle += 1
        show_crt()
        # aa = get_signal_strength(cycle, x_register)

        cycle += 1
        show_crt()
        # aa = get_signal_strength(cycle, x_register)

        x_register += int(line.split()[1])
        sprite_pos = [x_register-1, x_register, x_register+1]


# PART TWO: EJCFPGLH 
pprint([crt_row[40*x:40*(x+1)] for x in range(6)]) 

# print(sum(signals[:6]))
