import utils

lines = utils.read_input_lines(strip=True)
scores = {'X': 1, 'Y': 2, 'Z': 3}
mapping = {'A': 'X', 'B': 'Y', 'C': 'Z'}
winning = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
losing = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
draw = 3
win = 6


def get_score(a, b):
    if a == b:
        # Tie
        return scores[b] + draw
    elif b == winning[a]:
        # Win
        return scores[b] + win
    return scores[b]


score = 0
for line in lines:
    a, b = line.split(' ')
    a = mapping[a]
    score += get_score(a, b)

print(score)

score = 0
for line in lines:
    a, b = line.split(' ')
    a = mapping[a]
    if b == 'X':
        b = losing[a]
    elif b == 'Y':
        b = a
    else:
        b = winning[a]

    score += get_score(a, b)

print(score)
