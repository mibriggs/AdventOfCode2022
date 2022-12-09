import re

row_len = col_len = 0

def is_visible(height,trees, row, col):
    return (is_visible_helper(height, trees, row, col, 'RIGHT')
    or is_visible_helper(height, trees, row, col, 'LEFT')
    or is_visible_helper(height, trees, row, col, 'TOP')
    or is_visible_helper(height, trees, row, col, 'BOTTOM'))

def is_visible_helper(height, trees, row, col, direction):
    if is_edge(row, col):
        return True
    
    if direction == 'RIGHT':
        new_coord = (row, col+1)
        right_tree_height = trees.get(new_coord)
        return height > right_tree_height and is_visible_helper(height, trees, row, col + 1, direction)
    elif direction == 'LEFT':
        new_coord = (row, col-1)
        left_tree_height = trees.get(new_coord)
        return height > left_tree_height and is_visible_helper(height, trees, row, col - 1, direction)
    elif direction == 'TOP':
        new_coord = (row-1, col)
        top_tree_height = trees.get(new_coord)
        return height > top_tree_height and is_visible_helper(height, trees, row - 1, col, direction)
    elif direction == 'BOTTOM':
        new_coord = (row+1, col)
        bottom_tree_height = trees.get(new_coord)
        return height > bottom_tree_height and is_visible_helper(height, trees, row+1, col, direction)
    else:
        return False 

def is_edge(row, col):
    return row == 0 or row == (row_len-1) or col == 0 or col == (col_len-1)


def build_forest(file_path):
    forest = {}
    with open(file_path) as f:
        for row, line in enumerate(f):
            curr_row = [int(tree) for tree in re.findall('\d', line)]
            global col_len
            col_len += 1
            global row_len
            row_len = len(curr_row)
            for col, tree in enumerate(curr_row):
                forest[(row, col)] = tree
    return forest

def compute_scenic(height, forest, row, col):
    r = compute_scenic_helper(height, forest, row, col, 'RIGHT')
    l = compute_scenic_helper(height, forest, row, col, 'LEFT')
    t = compute_scenic_helper(height, forest, row, col, 'TOP')
    b = compute_scenic_helper(height, forest, row, col, 'BOTTOM')
    return (r * l * t * b)

def compute_scenic_helper(height, trees, row, col, direction):
    if is_edge(row, col):
        return 0
    
    if direction == 'RIGHT':
        new_coord = (row, col+1)
        right_tree_height = trees.get(new_coord)
        if height > right_tree_height:
            return 1 + compute_scenic_helper(height, trees, row, col + 1, direction)
        return 1
    elif direction == 'LEFT':
        new_coord = (row, col-1)
        left_tree_height = trees.get(new_coord)
        if height > left_tree_height:
            return 1 + compute_scenic_helper(height, trees, row, col - 1, direction)
        return 1
    elif direction == 'TOP':
        new_coord = (row-1, col)
        top_tree_height = trees.get(new_coord)
        if height > top_tree_height:
            return 1 + compute_scenic_helper(height, trees, row - 1 , col, direction)
        return 1
    elif direction == 'BOTTOM':
        new_coord = (row+1, col)
        bottom_tree_height = trees.get(new_coord)
        if height > bottom_tree_height:
            return 1 + compute_scenic_helper(height, trees, row + 1, col, direction)
        return 1
    else:
        return 0 



def main():
    count = 0
    scenics = []
    forest = build_forest('/Users/obriggs/Documents/Fall 2022/AdventOfCode/Day8/input.txt')
    for loc, height in forest.items():
        score = compute_scenic(height, forest, loc[0], loc[1])
        scenics.append(score)
        print(f'Tree located at: {loc} with a height of: {height} has a scenic score of: {score}')
    print(f"Maximum scenic score is: {max(scenics)}")
    #     if is_visible(height, forest, loc[0], loc[1]):
    #         count += 1
    #     print(f'Tree located at: {loc} with a height of: {height} is visible: {is_visible(height, forest, loc[0], loc[1])}')
    # print(count)

if __name__ == '__main__':
    main()