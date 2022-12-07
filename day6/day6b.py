WINDOW = 14

with open("day6/input") as f:
    input = f.read()

for i in range(WINDOW, len(input)+1):
    if len(set(input[i - WINDOW: i])) == WINDOW:
        print(i)
        break