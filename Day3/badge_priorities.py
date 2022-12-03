def find_badge(group):
    first, second, third = group
    for char in first:
        if char in second and char in third:
            return ord(char)
    return -1

def get_priority(letter):
    lower_start = ord('a')
    upper_start = ord('A')
    priority = 0
    if letter.islower():
        priority = (ord(letter) - lower_start) + 1
    else:
        priority = (ord(letter) - upper_start) + 27
    return priority

def get_groups(file_path):
    total_priority = 0
    with open(file_path) as f:
        file_lines = f.readlines()
        start, end = 0, 3
        while end <= len(file_lines):
            group = [item.rstrip('\n') for item in file_lines[start:end]]
            badge = find_badge(group)
            if badge > -1:
                 total_priority += get_priority(chr(badge))
            start += 3 
            end += 3
    print(total_priority)

def main():
    get_groups('test_input.txt')
    get_groups('inputs.txt')

if __name__ == '__main__':
    main()