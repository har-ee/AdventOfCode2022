import re
import numpy as np

class MonkeyTools:
    def __init__(self, monkey_list):
        self.map = {m.id: m for m in monkey_list}

class Monkey:
    operations = {'*': lambda x, y: x * y, '+': lambda x, y: x + y}

    def __init__(self, id, items, operator, oparg, test, on_true, on_false):
        self.id = id
        self.items = items
        self.operator = operator
        self.oparg = oparg
        self.test = test
        self.on_true = on_true
        self.on_false = on_false

        self.inspections = 0

    def parse_monkey(lines):
        id = int(re.search(r"Monkey (\d+)", lines).groups()[0])
        items_str = re.search(r"Starting items: (.*)", lines).groups()[0]
        items = [int(i) for i in items_str.split(", ")]
        _, operator, oparg = re.search(
            r"Operation: new = ([a-z0-9]+) ([+*]) ([a-z0-9]+)", lines).groups()
        test = int(re.search(r"Test: divisible by (\d+)", lines).groups()[0])
        on_true = int(re.search(r"If true: throw to monkey (\d+)", lines).groups()[0])
        on_false = int(re.search(r"If false: throw to monkey (\d+)", lines).groups()[0])

        return Monkey(id, items, operator, oparg, test, on_true, on_false)

    def do_operation(self, item):
        term = item if self.oparg == 'old' else int(self.oparg)
        new_worry = Monkey.operations[self.operator](item, term)
        return int(new_worry / 3)

    def throw(self, worry, tools):
        passed_test = worry % self.test == 0
        to_monkey = self.on_true if passed_test else self.on_false
        tools.map[to_monkey].items.append(worry)

    def do_turn(self, tools):
        for item in self.items:
            self.inspections += 1
            item_worry = self.do_operation(item)
            self.throw(item_worry, tools)
        self.items = []


with open("day11/input") as f:
    monkey_list = [Monkey.parse_monkey(m) for m in f.read().split("\n\n")]

monkey_tools = MonkeyTools(monkey_list)

for _ in range(20):
    [monkey.do_turn(monkey_tools) for monkey in monkey_list]

inspections = [m.inspections for m in monkey_list]
result = np.prod(sorted(inspections)[-2:])

print(result)
