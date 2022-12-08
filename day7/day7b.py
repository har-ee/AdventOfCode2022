import re

class Dir:
    def __init__(self, path, parent):
        self.path = path
        self.parent = parent
        self.dirs = set()  # dirs
        self.files = {}  # files # Name: size

    def add_dir(self, dir):
        self.dirs.add(dir)

    def add_file(self, filename, size):
        self.files[filename] = size

    def size(self):
        file_size = sum([v for (_, v) in self.files.items()])
        dir_size = sum([d.size() for d in self.dirs])
        return file_size + dir_size

with open("day7/input") as f:
    inp = f.read()

dir = Dir("", None)
dirs = {"": dir}

matches = re.findall(
    r"^(\$ )?(?:(cd|ls)|([a-zA-Z0-9]+))(?: ([a-zA-Z0-9./]+))?", inp, re.M)
for match in matches:
    prompt, cmd, arg1, arg2 = match
    if prompt:
        if cmd == "cd":
            if arg2 == "..":
                dir = dir.parent
            elif arg2 == "/":
                dir = dirs[""]
            else:
                dir = dirs[dir.path + "/" + arg2]
    else:
        if arg1 == "dir":
            child = Dir(dir.path + "/" + arg2, dir)
            dir.add_dir(child)
            dirs[child.path] = child
        else:
            dir.add_file(arg2, int(arg1))

total = dirs[""].size()
req = total - (70000000 - 30000000)
sizes = [d.size() for (_, d) in dirs.items() if d.size() > req]

print(min(sizes))
