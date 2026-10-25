import random

state = [1, 2, 3, 4, 5, 6, 0, 7, 8]

def get_valid_moves(state):
    zero_index = state.index(0)
    zero_index_row = zero_index // 3

    row_neighbours = []
    left = zero_index - 1
    right = zero_index + 1  
 
    #Horizontal moves
    if left // 3 == zero_index_row:
         row_neighbours.append(left)
    if right // 3 == zero_index_row:
             row_neighbours.append(right)    
         
    #Vertical moves
    if zero_index + 3 <= len(state) -1:
           row_neighbours.append(zero_index + 3) 
    if zero_index - 3 >= 0:
        row_neighbours.append(zero_index - 3)
    return row_neighbours

def generate_next_states(state):
    valid_moves = get_valid_moves(state)
    move_collection = []
    for move in valid_moves:
        new_list = state.copy()
        index_for_0_value = new_list.index(0)
        new_list[index_for_0_value], new_list[move] = new_list[move], new_list[index_for_0_value]
        move_collection.append(new_list)
    return move_collection

generate_next_states(state)

#tests

state_corner = [1, 2, 3, 4, 5, 6, 0, 7, 8]
state_center = [1, 2, 3, 4, 0, 5, 6, 7, 8]
state_edge = [1, 0, 2, 3, 4, 5, 6, 7, 8]

assert len(generate_next_states(state_corner)) == 2
assert len(generate_next_states(state_center)) == 4
assert len(generate_next_states(state_edge)) == 3

state = [1, 2, 3, 4, 0, 5, 6, 7, 8]

original_state = state.copy()

generate_next_states(state)

assert state == original_state

successors = generate_next_states(state)

for successor in successors:
    assert sorted(successor) == list(range(9))

state = [1, 2, 3, 4, 0, 5, 6, 7, 8]

first_result = generate_next_states(state)
second_result = generate_next_states(state)

assert first_result == second_result

state = [4, 2, 3, 5, 1, 6, 0, 7, 8]

def count_inversions(state):
    inversion_count = 0
    for index, currentState in enumerate(state):
        if currentState == 0:
            continue
        for x in state[index + 1:]:
            if x == 0:
                 continue
            if currentState > x:
                inversion_count += 1
    return inversion_count
count_inversions(state)

#tests
assert count_inversions([1, 2, 3, 4, 5, 6, 7, 8, 0]) == 0
assert count_inversions([2, 1, 3, 4, 5, 6, 8, 7, 0]) == 2
assert count_inversions([3, 2, 1, 4, 5, 6, 7, 8, 0]) == 3
assert count_inversions([8, 7, 6, 5, 4, 3, 2, 1, 0]) == 28

def is_solvable(state):
     inversion_count = count_inversions(state)
     return inversion_count % 2 == 0

#tests
assert is_solvable([1, 2, 3, 4, 5, 6, 7, 8, 0]) == True
assert is_solvable([1, 2, 3, 4, 5, 6, 8, 7, 0]) == False
assert is_solvable([2, 1, 3, 4, 5, 6, 8, 7, 0]) == True

def generate_random_state():
    while True:
        numbers = list(range(9))
        random.shuffle(numbers)
        if is_solvable(numbers):
            return numbers           
generate_random_state()

#tests
random_state = generate_random_state()

assert len(random_state) == 9
assert sorted(random_state) == list(range(9))
assert is_solvable(random_state)

for i in range(100):
    new_state = generate_random_state()
    assert is_solvable(new_state),  f"Invalid state: {new_state}"

current_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]

g_scores = {
    tuple(current_state): 4
}

next_states = generate_next_states(current_state)

for state in next_states:
    state_tuple = tuple(state)
    new_g = g_scores[tuple(current_state)] + 1
    if state_tuple not in g_scores or new_g < g_scores[state_tuple]:
        g_scores[state_tuple] = new_g
print(g_scores)

state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
def hamming_distance(state):
    misplaced_tiles = 0
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for index, tile in enumerate(state):
        if tile != goal_state[index] and tile != 0:
            misplaced_tiles += 1
    return misplaced_tiles
hamming_distance(state)

#tests
assert hamming_distance([1, 2, 3, 4, 5, 6, 7, 8, 0]) == 0

assert hamming_distance([1, 2, 3, 4, 5, 6, 7, 0, 8]) == 1

assert hamming_distance([1, 2, 3, 4, 5, 6, 0, 7, 8]) == 2

assert hamming_distance([1, 2, 3, 4, 0, 6, 7, 5, 8]) == 2