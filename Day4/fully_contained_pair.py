def check_pairs(file_path):
    contained_total = 0
    overlap_total = 0
    with open(file_path) as f:
        for line in f:
            left, right = line.rstrip('\n').split(',')
            left = [int(char) for char in left.split('-') if not char == '-']
            right = [int(char) for char in right.split('-') if not char == '-']
            if is_fully_contained(left, right):
                overlap_total += 1
                contained_total += 1
            elif does_overlap(left, right):
                overlap_total += 1
    print(contained_total)
    print(overlap_total)

def is_fully_contained(range1, range2):
    return ((range1[0] >= range2[0] and range1[1] <= range2[1]) or (range2[0] >= range1[0] and range2[1] <= range1[1]))

def does_overlap(range1, range2):
    return (
        range1[0] >= range2[0] and range1[0] <= range2[1] or
        range1[1] >= range2[0] and range1[1] <= range2[1] or
        range2[0] >= range1[0] and range2[0] <= range1[1] or
        range2[1] >= range1[0] and range2[1] <= range1[1]
    )


def main():
    check_pairs('test_input.txt')
    check_pairs('input.txt')

if __name__ == '__main__':
    main()
