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
        new_list[new_list.index(0)], new_list[move] = new_list[move], new_list[new_list.index(0)]
        move_collection.append(new_list)
    return move_collection

generate_next_states(state)