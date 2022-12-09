import numpy as np

directions = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}

def move_head(point, direction):
    return np.add(point, directions[direction])

def move_tail_segment(tail, head):
    dx, dy = np.subtract(head, tail)

    if (calc_distance(abs(dx), abs(dy)) <= 1):
        return tail

    return np.add(tail, [np.sign(dx), np.sign(dy)])

def calc_distance(dx, dy):
    return (dx if dx == dy else dx + dy)

with open("day9/input") as f:
    inp = f.read().splitlines()
    split = [l.split(' ') for l in inp]
    parsed = [(direction, int(distance)) for direction, distance in split]

head = np.array([0, 0])
tail = np.array([0, 0])
visited = set()

for (direction, distance) in parsed:
    for _ in range(distance):
        head = move_head(head, direction)
        tail = move_tail_segment(tail, head)
        visited.add(tail.tobytes())

print(len(visited))