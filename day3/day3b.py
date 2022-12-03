import string

def score(c):
    return string.ascii_letters.index(c) + 1

f = open("day3/input")
raw = f.read()
f.close()

parsed = [set(l) for l in raw.split('\n')]

result = 0
for i in range(0, len(parsed), 3):
    group = parsed[i:i+3]
    badge = set.intersection(*group).pop()
    result += score(badge)

print(result)
