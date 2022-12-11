import re

with open("day4/input") as f:
    raw = f.read()

result = 0

matches = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", raw)
for raw_match in matches:
    start_1, end_1, start_2, end_2 = map(int, raw_match)
    set_1 = set(range(start_1, end_1+1))
    set_2 = set(range(start_2, end_2+1))

    if (set_1.intersection(set_2) != set()):
        result += 1

print(result)
