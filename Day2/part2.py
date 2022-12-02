letter_to_shape = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

shape_to_outcome = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

shape_to_points = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}

def choice_for_win(oponnent_shape):
    winnning_shape = ''
    if oponnent_shape == 'ROCK':
        winnning_shape = 'PAPER'
    elif oponnent_shape == 'PAPER':
        winnning_shape = 'SCISSORS'
    else:
        winnning_shape = 'ROCK'
    return winnning_shape

def choice_for_loss(oponnent_shape):
    winnning_shape = ''
    if oponnent_shape == 'ROCK':
        winnning_shape = 'SCISSORS'
    elif oponnent_shape == 'PAPER':
        winnning_shape = 'ROCK'
    else:
        winnning_shape = 'PAPER'
    return winnning_shape

def choice_for_tie(oponnent_shape):
    return oponnent_shape

def compute_my_choice(oponnent_letter, desired_outcome):
    oponnent_shape = letter_to_shape[oponnent_letter]
    my_shape = ''
    if desired_outcome == 6:
        my_shape = choice_for_win(oponnent_shape)
    elif desired_outcome == 3:
        my_shape = choice_for_tie(oponnent_shape)
    else:
        my_shape = choice_for_loss(oponnent_shape)
    return my_shape

def compute_round_score(opponent_choice, my_choice):
    desired_outcome = shape_to_outcome[my_choice]
    my_score = shape_to_points[compute_my_choice(opponent_choice, desired_outcome)] + desired_outcome
    return my_score

def compute_total_score(file_path):
    my_total = 0
    with open(file_path) as f:
        for line in f:
            opp, me = line.split()
            my_score = compute_round_score(opp, me)
            my_total += my_score
    print(my_total)

def main():
    compute_total_score('test_input.txt')
    compute_total_score('inputs.txt')

if __name__ == '__main__':
    main()
