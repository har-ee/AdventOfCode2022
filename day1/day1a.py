f = open("day1/input")

raw = f.read()
parsed = [map(int, x.split('\n')) for x in raw.split("\n\n")]
calories = map(sum, parsed)
answer = max(calories)
print(answer)

f.close()