import numpy as np

def check_vision(coords, height):
    i = 0
    for i, (x, y) in enumerate(coords):
        tree_h = matrix[y][x]
        if tree_h >= height:
            break
    return i + 1

with open("day8/input") as f:
    inp = f.read().splitlines()
    matrix = [list(map(int, l)) for l in inp]

max_score = 0
h, w = np.shape(matrix)

for y, x in np.ndindex(h, w):
    height = matrix[y][x]

    coords = [[(x, i) for i in range(y-1, -1, -1)]]     # Up
    coords.append([(x, i) for i in range(y+1, h, 1)])   # Down
    coords.append([(i, y) for i in range(x-1, -1, -1)]) # Left
    coords.append([(i, y) for i in range(x+1, w, 1)])   # Right

    score = np.prod([check_vision(c, height) for c in coords])

    if (score > max_score):
        max_score = score

print(max_score)