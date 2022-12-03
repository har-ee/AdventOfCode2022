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

    if wins_vs[m1] == m2:
        return 0 + pts
    if m1 == m2:
        return 3 + pts
    return 6 + pts


f = open("day2/input")
raw = f.read()
f.close()

parsed = [l.split(' ') for l in raw.split('\n')]
parsed = [[moves[x], moves[y]] for x, y in parsed]

scores = [score(x, y) for x, y in parsed]
result = sum(scores)

print(result)