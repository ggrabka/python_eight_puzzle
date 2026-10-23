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