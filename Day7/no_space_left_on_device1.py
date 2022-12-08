from FileSystem import FileSystem, File

MAX_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
MIN_FREE_SPACE = 30000000

def handle_command(line):
    _, _, directory = line.split()
    return directory

def add_child(current_folder: FileSystem, line: str):
    if 'dir' in line:
        _, new_dir = line.split()
        print(f'[INFO] Adding Sub-Directory: {new_dir}')
        if new_dir not in current_folder.sub_folders:
            current_folder.add_child(FileSystem(new_dir, parent=current_folder))
    else:
        file_size, file_name = line.split()
        new_file = File(file_name, file_size)
        current_folder.add_file(new_file)
        print(f'[INFO] Adding file: {file_name} of size: {file_size} to directory: {current_folder.name}')

def compute_directories(file_system, so_far):
    directory_size = file_system.get_size()
    if directory_size <= MAX_SIZE:
        so_far.append(file_system)
    for sub_dir in file_system.sub_folders:
        compute_directories(sub_dir, so_far)
    return so_far

def compute_deletable(file_system, so_far, min_size):
    directory_size = file_system.get_size()
    if directory_size >= min_size:
        so_far.append((directory_size, file_system))
    for sub_dir in file_system.sub_folders:
        compute_deletable(sub_dir, so_far, min_size)
    return so_far

def build_file_system(file_path):
    home = FileSystem('/')
    with open(file_path) as f:
        current_folder = home
        for line in f:
            if current_folder == None:
                pass
            line = line.strip('\n')
            if line[0] == '$' and 'cd' in line:
                directory_to_move_to = handle_command(line)
                print(f'[INFO] Moving into a directory: {directory_to_move_to}')
                if directory_to_move_to == '/':
                    current_folder = home
                elif directory_to_move_to == '..':
                    current_folder = current_folder.parent
                else:
                    new_child = FileSystem(directory_to_move_to, current_folder)
                    if new_child not in current_folder.sub_folders:
                        current_folder.add_child(new_child)
                    current_folder = current_folder.get_sub_folder(new_child)
            elif line.split()[1] == 'ls':
                print(f'[INFO] Printing files and sub folders in directory: {current_folder.name}')
            else:
                add_child(current_folder, line)
    return home

def get_directories_that_match(file_system):
    print('--------------------------------------- Printing directories that match --------------------------------------')
    directories_that_fit = []
    compute_directories(file_system, directories_that_fit)
    total = 0
    for match in directories_that_fit:
        print(match)
        total += match.get_size()
    print(f'Size of all directories that meet criteria is: {total}')

def get_directories_to_delete(file_system):
    print('--------------------------------------- Printing directories that can be deleted --------------------------------------')
    current_free_space = TOTAL_DISK_SPACE - file_system.get_size()
    space_to_free = MIN_FREE_SPACE - current_free_space
    print(f'Must free at least: {space_to_free} bytes')
    deletable = []
    compute_deletable(file_system, deletable, space_to_free)
    deletable = sorted(deletable, key=lambda x: x[0])
    for can_delete in deletable:
        print(f'Size: {can_delete[0]}\n{can_delete[1]}')
    size, fs = deletable[0]
    print(f'Smallest deletable directory is: {fs} with a size of {size}')

def main():
    test_file = '/Users/obriggs/Documents/Fall 2022/AdventOfCode/Day7/test_input.txt'
    real_file = '/Users/obriggs/Documents/Fall 2022/AdventOfCode/Day7/input.txt'
    test_home = build_file_system(test_file)
    print('\n' + str(test_home))
    get_directories_that_match(test_home)
    get_directories_to_delete(test_home)
    print()
    real_home = build_file_system(real_file)
    print('\n' + str(real_home))
    get_directories_that_match(real_home)
    get_directories_to_delete(real_home)

if __name__ == '__main__':
    main()
