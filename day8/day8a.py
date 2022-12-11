import numpy as np

def visible_height(row):
    height = -1
    return [(height := i) if i > height else height + 1 for i in row]

def visible_left(matrix):
    return [visible_height(row) for row in matrix]

def visible_matrix(matrix):
    views = [np.rot90(visible_left(np.rot90(matrix, i)), 4-i) for i in range(4)]

    h, w = np.shape(matrix)
    visible = np.empty([h,w])

    for x, y in np.ndindex(h, w):
        visible[y][x] = min([m[y][x] for m in views])
    return visible

def visible_trees(matrix):
    h, w = np.shape(matrix)
    heights = visible_matrix(matrix)
    return len([1 for x, y in np.ndindex(h, w) if heights[y][x] <= matrix[y][x]])

with open("day8/input") as f:
    inp = f.read().splitlines()
    parsed = [list(map(int, l)) for l in inp]

print(visible_trees(parsed))
