strategy = [line.strip().upper() for line in open("aoc2022/day2.txt")]

player_score = 0
# [enemy player] each round
player_wins = ['A Y', 'B Z', 'C X']
player_draw = ['A X', 'B Y', 'C Z']
player_lose = ['A Z', 'B X', 'C Y'] #for PART TWO
choices_score = {'X': 1, 'Y': 2, 'Z': 3}

# PART TWO
def play_round(play_strategy, enemy_choice):
    for i in play_strategy:
        if i[0] == enemy_choice:
            # e.g. return 'A Z'
            return i

for round in strategy:
    
    # PART TWO
    strategy_map = {'X': player_lose, 'Y': player_draw, 'Z': player_wins}
    # select the appropriate weapon for the player
    # like the part one round value
    enemy_choice = round[0]
    player_choice = round[2]
    # comment "round" to get the part ONE answer
    round = play_round(strategy_map[player_choice], enemy_choice) 

    
    # PART ONE
    if round in player_wins:
        player_score += 6
    elif round in player_draw:
        player_score += 3
    else:
        # print('lost')
        pass
    
    player_score += choices_score[round[2]]

print(player_score)

'''
secrets = [line.strip().upper().split() for line in open('day2.txt')]
counter = 0
player_score = 0
for enemy, player in secrets:
    if enemy == player:
        score = 3
    elif enemy == 'A' and player == 'Y':
        score = 6
    elif enemy == 'B' and player == 'Z':
        score = 6
    elif enemy == 'C' and player == 'X':
        score = 6
    else:
        score = 0
    choice_score = {'X': 1, 'Y': 2, 'Z': 3}
    player_score += (score + choice_score[player])
    # print(enemy, player, score, choice_score[player], (score + choice_score[player]), player_score)
    # counter += 1
    if counter >= 6:
        break
print(player_score)
'''


'''
A rock B paper C scissor

X rock Y paper Z scissor
  1      2       3

lost 0 draw 3 won 6
(enemy player)
(A Y)

For the PART TWO:

X to lose
Y to draw
Z to win
'''