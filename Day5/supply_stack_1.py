import re

class Queue:
    def __init__(self, arr=[]) -> None:
        self.__items: list = arr

    def enqueue(self, elem) -> None:
        self.__items.insert(0, elem)
    
    def dequeue(self) -> int:
        removed_element = self.__items.pop(0)
        return removed_element
    
    def __str__(self) -> str:
        return str(self.__items)

def split_input(file_path: str) -> tuple:
    crates = ''
    with open(file_path) as f:
        for i, line in enumerate(f):
            if line in ['\n', '\r\n']:
                break
            else:
                crates += line
        moves = f.readlines()
    return (crates, moves)

def make_dict(arr):
    my_dict = {}
    for row in arr:
        new_str = ''
        for i, char in enumerate(row):
            indx = i + 1
            if char != ' ':
                new_str += char
            if indx%4 == 0:
                new_str += ' '
            elif char == ' ':
                new_str += '-'
        stacks = new_str.split()
        for i, crate in enumerate(stacks):
            if crate != '---':
                indx = i + 1
                if indx not in my_dict:
                    my_dict[indx] = [crate[1]]
                else:
                    my_dict[indx].append(crate[1])

    for key, val in my_dict.items():
        my_dict[key] = Queue(val)
    return my_dict

def compute_move(move, stacks):
    pattern = '\d+'
    match = re.findall(pattern, move)
    amount, from_pos, to_pos = [int(num) for num in match]
    
    while amount > 0:
        val = stacks[from_pos].dequeue()
        stacks[to_pos].enqueue(val)
        amount = amount - 1

def handle_moves(moves, stacks):
    for move in moves:
        compute_move(move, stacks)

def find_ending_stacks(file_path):
    crates, moves = split_input(file_path)
    crates_arr = crates.split('\n')
    crates_arr = crates_arr[:len(crates_arr)-2]
    stacks = make_dict(crates_arr)
    for key in sorted(stacks):
        print(f'{key}:{stacks[key]}')
    print('')
    handle_moves(moves, stacks)
    for key in sorted(stacks):
        print(f'{key}:{stacks[key]}')


def main():
    # find_ending_stacks('test_input.txt')
    find_ending_stacks('inputs.txt')
    

if __name__ == '__main__':
    main()
