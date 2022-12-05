import re

def parse_towers(inp):
    inp_transposed = [''.join(reversed(col)) for col in zip(*inp)]

    stacks = [re.search(r"[A-Z]+", row) for row in inp_transposed]
    stacks = [list(x.group(0)) for x in stacks if x != None]

    stack_dict = {(i+1): stack for i, stack in enumerate(stacks)}
    return stack_dict

def move(stack_dict, amount, source, destination):
    stack_dict[destination].extend(stack_dict[source][-amount:])
    del stack_dict[source][-amount:]

with open("day5/input") as f:
    raw_towers, raw_moves = f.read().split("\n\n")

stack_dict = parse_towers(raw_towers.splitlines())

matches = re.findall(r"move (\d+) from (\d+) to (\d+)", raw_moves)
for match in matches:
    amount, source, destination = map(int, match)
    move(stack_dict, amount, source, destination)

result = ''.join([v.pop() for (_, v) in stack_dict.items()])

print(result)
