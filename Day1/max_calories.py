def max_calories(file_name):
    calories = []
    with open(file_name) as f:
        seen_so_far = 0
        for line in f:
            if line == '\n':
                calories.append(seen_so_far)
                seen_so_far = 0
            else:
                seen_so_far += int(line) 
    
    calories.sort(reverse=True)
    print(sum(calories[:3]))
    print(calories[0])


def main():
    FILE = 'calories.txt'
    max_calories(FILE)

if __name__ == '__main__':
    main()
