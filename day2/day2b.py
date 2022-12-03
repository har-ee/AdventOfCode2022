R = "ROCK"
P = "PAPER"
S = "SCISSORS"

bonus = {
    R: 1, P: 2, S: 3,
}

wins_vs = {
    R: S, P: R, S: P,
}

moves = {
    "A": R, "B": P, "C": S,
    "X": R, "Y": P, "Z": S,
}


def score(m1, m2):
    pts = bonus[m2]
    if m1 == m2:
        return 3 + pts
    if wins_vs[m1] == m2:
        return 0 + pts
    return 6 + pts


def choose(m1, outcome):
    if (outcome == 'X'): # Lose
        return wins_vs[m1]
    elif (outcome == 'Y'): # Draw
        return m1
    else: # Win
        move_set = {R, P, S}
        return move_set.difference({m1, wins_vs[m1]}).pop()


f = open("day2/input")
raw = f.read()
f.close()

parsed = [l.split(' ') for l in raw.split('\n')]
parsed = [[moves[x], y] for x, y in parsed]

scores = [score(x, choose(x, y)) for x, y in parsed]
result = sum(scores)

print(result)