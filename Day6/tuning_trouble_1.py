def get_all_substrings(string, max_length):
    answ = []
    for i in range(0, len(string) - (max_length - 1)):
        text = f'{string[i]}'
        j = i+1
        while len(text) < max_length:
            text += string[j]
            j += 1
        answ.append(text)
    return answ


def get_start_marker(signal, max_length):
    choices = get_all_substrings(signal, max_length)
    substring = ''
    for choice in choices:
        unique = list(set(choice))
        orig = list(choice)
        unique.sort()
        orig.sort()
        if unique == orig:
            substring = choice
            break
    return signal.index(substring) + max_length

def get_all_markers(file_path):
    with open(file_path) as f:
        for line in f:
            line = line.strip('\n')
            marker = get_start_marker(line, 4)
            message = get_start_marker(line, 14)
            print(f'Buffer: {line}, Marker start: {marker}, Message start: {message}')

def main():
    get_all_markers('test_input.txt')
    get_all_markers('input.txt')

if __name__ == '__main__':
    main()