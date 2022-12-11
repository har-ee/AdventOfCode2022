import re

with open("day10/input") as f:
    inp = f.read()
    instrs = list(re.findall(r"([a-z]+) ?(-?\d+)?", inp))

cycles = 1
instr_pointer = 0
x = 1
trigger_time = 0
pending = 0
store = []

while (instr_pointer < len(instrs) or trigger_time >= cycles):
    if (cycles + 20) % 40 == 0:
        store.append(cycles*x)

    if trigger_time >= cycles:
        if cycles == trigger_time:
            x += pending
            instr_pointer += 1
    else:
        command, istr = instrs[instr_pointer]
        if command == "addx":
            trigger_time = cycles + 1
            pending = int(istr)
        else:
            instr_pointer += 1

    cycles += 1

print(sum(store))
