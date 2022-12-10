from pprint import pprint
from collections import defaultdict

def reader(file):
    with open(file, "r") as f:
        lines = [line.split(",")[0] for line in  f.read().splitlines()]
    return lines

class Directory():
    
    def __init__(self, name, parent=set(), level=0, path=[]):
        self.name = name
        self.folders = []
        self.parent = parent
        self.files = []
        self.total_size = 0
        self.level = level
        self.path = "/".join(path)
    
    def __repr__(self):
        return f"DIR {self.name}"
    
    def add_file(self, filename, filesize):
        new_file = (filename, filesize)
        self.total_size += filesize
        self.files.append(new_file)

        



def build_tree(instructions):
    root = Directory(name=".", path=["."])
    #directories = {f"{root.name}":root}
    directories = {f"{root.path}":root}
    current_dir_path = [root.path]

    # path to string helper function
    def p2s(path):
        return "/".join(path)

    level = 0
    for command in instructions[1:]:
        # directory movement
        if command.startswith("$ cd"): 
            target_dir = command.split(" ")[2]
            if target_dir == "..":
                current_dir_path.pop()
                level -= 1
            else:
                current_dir_path.append(target_dir )
                level +=1
        # ls informations
        # information of folders in directory
        if command.startswith("dir"):
            #folder_name = command.split(" ")[1]
            path_name = command.split(" ")[1]
            #if folder_name not in directories:
            if path_name not in directories:
                #directories[folder_name] = Directory(name=folder_name,
                directories[p2s(current_dir_path+[path_name])] = Directory(name=path_name,
                                                     parent=p2s(current_dir_path),
                                                     level=level+1,
                                                     path=current_dir_path)
                #directories[current_dir_path[-1]].folders.append(folder_name)
                directories[p2s(current_dir_path)].folders.append(path_name)
                #print(vars(directories[folder_name]))

        # information of files in directory
        elif command.startswith("$") == False:
            file_size = int(command.split(" ")[0])
            file_name = command.split(" ")[1]
            #if file_name not in directories[current_dir_path[-1]].files:
            if file_name not in directories[p2s(current_dir_path)].files:
                directories[p2s(current_dir_path)].add_file(filename=file_name, filesize=file_size)

    return directories


def update_total_sizes(directories, maxlevel):
    dirs_left = len(directories)
    size_folders = defaultdict(int)
    while dirs_left > 1:
        for stage in reversed(range(1, maxlevel+1)):
            for dirname, dir in directories.items():
                if dir.level == stage:
                    directories[dir.parent].total_size += dir.total_size
                    dirs_left -= 1                    
                else:
                    pass

    for dirname, dir in directories.items():
        size_folders[dirname] += dir.total_size

    return size_folders

def get_max_level(directories):
    mlevel = max([dir.level for name, dir in directories.items()])
    return mlevel

def get_final_sum(sizes, max_limit):
    valid_sizes = [size for dir, size in sizes.items() if size <= max_limit]
    sum_val_size = sum(valid_sizes)
    return sum_val_size

def get_closest(sizes, available, needed):
    unused = available - sizes["."]
    needed = needed - unused
    deltas = {}
    for i, (dir_name, size) in enumerate(sizes.items()):
        delta = size - needed
        if delta >= 0:
            deltas[delta] = size
    sort_delt = sorted(deltas.items())
    min_size = sort_delt[0][1]
        
    return min_size

def result(lines):
    filesystem = build_tree(lines)
    max_level = get_max_level(directories=filesystem)
    sizes = update_total_sizes(directories=filesystem, maxlevel=max_level)
    #res=get_final_sum(sizes, max_limit=100_000)
    res = get_closest(sizes, available=70_000_000, needed=30_000_000)
    

    return res


if __name__ == "__main__":
    lines = reader("input.txt")
    res = result(lines)

    print(res)



    
