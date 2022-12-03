import string

def duplicate(l):
    mid = int(len(l)/2)
    return set.intersection(set(l[:mid]),set(l[mid:])).pop()

def score(c):
    return string.ascii_letters.index(c) + 1

f = open("day3/input")
raw = f.read()
f.close()

parsed = raw.split('\n')

scores = [score(duplicate(c)) for c in parsed]
result = sum(scores)

print(result)
