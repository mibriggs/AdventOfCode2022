def binary_search(arr, low, high, x):
 
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
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


def split_sack(rucksack_items):
    mid_point = len(rucksack_items)//2
    compartment1, compartment2 = rucksack_items[:mid_point], rucksack_items[mid_point:]
    compartment2 = ''.join(sorted(compartment2))
    priorities_so_far = 0
    seen_letters = []
    for char in compartment1:
        indx = binary_search(compartment2, 0, len(compartment2)-1, char)
        if indx > -1 and char not in seen_letters:
            priority = get_priority(char)
            priorities_so_far += priority
        seen_letters.append(char)
    return priorities_so_far

def get_duplicates(file_path):
    total_priorities = 0
    with open(file_path) as f:
        for line in f:
            priority = split_sack(line)
            total_priorities += priority
    print(total_priorities)

def main():
    get_duplicates('test_input.txt')
    get_duplicates('inputs.txt')

if __name__ == '__main__':
    main()