letter_to_shape = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

shape_to_points = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}
'''
    MY CHOICE | OTHER CHOICE
    -------------------------
        R     |     R  --> 1 - 1 = 0 --> Draw
        R     |     P  --> 1 - 2 = -1 --> Loss
        R     |     S  --> 1 - 3 = -2 --> Win
    -------------------------
        P     |     R  --> 2 - 1 = 1 --> Win
        P     |     P  --> 2 - 2 = 0 --> Draw
        P     |     S  --> 2 - 3 = -1 --> Loss
    -------------------------
        S     |     R  --> 3 - 1 = 2 --> Loss
        S     |     P  --> 3 - 2 = 1 --> Win
        S     |     S  --> 3 - 3 = 0 --> Draw

'''
def round_outcome(opponet_shape, my_shape):
    point_differential = shape_to_points[my_shape] - shape_to_points[opponet_shape]
    if point_differential == 0:
        return 3
    elif point_differential == -2 or point_differential == 1:
        return 6
    else:
        return 0

def compute_round_score(opponent_choice, my_choice):
    opponet_shape = letter_to_shape[opponent_choice]
    my_shape = letter_to_shape[my_choice]
    my_score = round_outcome(opponet_shape, my_shape) + shape_to_points[my_shape]
    opponent_score = round_outcome(my_shape, opponet_shape) + shape_to_points[opponet_shape]
    return (opponent_score, my_score)

def compute_total_score(file_path):
    my_total = 0
    opp_total = 0
    with open(file_path) as f:
        for line in f:
            opp, me = line.split()
            opp_score, my_score = compute_round_score(opp, me)
            my_total += my_score
            opp_total += opp_score
    print(my_total)

def main():
    compute_total_score('test_input.txt')
    compute_total_score('inputs.txt')

if __name__ == '__main__':
    main()
