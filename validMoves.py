import random
import heapq
import time

state = [1, 2, 3, 4, 5, 6, 0, 7, 8]


def get_valid_moves(state):
    zero_value_index = state.index(0)
    zero_value_index_row = zero_value_index // 3

    row_neighbours = []
    left = zero_value_index - 1
    right = zero_value_index + 1

    # Horizontal moves
    if left // 3 == zero_value_index_row:
        row_neighbours.append(left)
    if right // 3 == zero_value_index_row:
        row_neighbours.append(right)

    # Vertical moves
    if zero_value_index + 3 <= len(state) - 1:
        row_neighbours.append(zero_value_index + 3)
    if zero_value_index - 3 >= 0:
        row_neighbours.append(zero_value_index - 3)
    return row_neighbours


def generate_next_states(state):
    valid_moves = get_valid_moves(state)
    move_collection = []
    for move in valid_moves:
        new_list = list(state).copy()
        zero_value_index = new_list.index(0)
        new_list[zero_value_index], new_list[move] = (
            new_list[move],
            new_list[zero_value_index],
        )
        move_collection.append(new_list)
    return move_collection


generate_next_states(state)

# tests

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
        for x in state[index + 1 :]:
            if x == 0:
                continue
            if currentState > x:
                inversion_count += 1
    return inversion_count


count_inversions(state)

# tests
assert count_inversions([1, 2, 3, 4, 5, 6, 7, 8, 0]) == 0
assert count_inversions([2, 1, 3, 4, 5, 6, 8, 7, 0]) == 2
assert count_inversions([3, 2, 1, 4, 5, 6, 7, 8, 0]) == 3
assert count_inversions([8, 7, 6, 5, 4, 3, 2, 1, 0]) == 28


def is_solvable(state):
    inversion_count = count_inversions(state)
    return inversion_count % 2 == 0


# tests
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

# tests
random_state = generate_random_state()

assert len(random_state) == 9
assert sorted(random_state) == list(range(9))
assert is_solvable(random_state)

for i in range(100):
    new_state = generate_random_state()
    assert is_solvable(new_state), f"Invalid state: {new_state}"

current_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]

g_scores = {tuple(current_state): 4}

next_states = generate_next_states(current_state)

for state in next_states:
    state_tuple = tuple(state)
    new_g = g_scores[tuple(current_state)] + 1
    if state_tuple not in g_scores or new_g < g_scores[state_tuple]:
        g_scores[state_tuple] = new_g
print(g_scores)

state = [1, 2, 3, 4, 5, 6, 0, 7, 8]


def calculate_hamming_distance(state):
    misplaced_tiles = 0
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for index, tile in enumerate(state):
        if tile != goal_state[index] and tile != 0:
            misplaced_tiles += 1
    return misplaced_tiles


calculate_hamming_distance(state)

# tests
assert calculate_hamming_distance([1, 2, 3, 4, 5, 6, 7, 8, 0]) == 0

assert calculate_hamming_distance([1, 2, 3, 4, 5, 6, 7, 0, 8]) == 1

assert calculate_hamming_distance([1, 2, 3, 4, 5, 6, 0, 7, 8]) == 2

assert calculate_hamming_distance([1, 2, 3, 4, 0, 6, 7, 5, 8]) == 2


def get_row_and_column(state):
    coordinates = {}
    tiles_dimension = 3
    for index, tile in enumerate(state):
        coordinates[tile] = [index // tiles_dimension, index % tiles_dimension]
    return coordinates


get_row_and_column(state)

current_coordinates = get_row_and_column(state)
goal_coordinates = get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0])


def calculate_manhattan_distance(current_coordinates, goal_coordinates):
    distance = {}
    for tile in current_coordinates:
        if tile == 0:
            continue
        distance[tile] = abs(
            current_coordinates[tile][0] - goal_coordinates[tile][0]
        ) + abs(current_coordinates[tile][1] - goal_coordinates[tile][1])
    return sum(distance.values())


calculate_manhattan_distance(current_coordinates, goal_coordinates)

# tests
assert (
    calculate_manhattan_distance(
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0]),
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0]),
    )
    == 0
)

assert (
    calculate_manhattan_distance(
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 0, 8]),
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0]),
    )
    == 1
)

current_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]

g_scores = {tuple(current_state): 0}

goal_coordinates = get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0])

hamming_score = calculate_hamming_distance(current_state)
manhattan_score = calculate_manhattan_distance(
    get_row_and_column(current_state), goal_coordinates
)
current_score = g_scores[tuple(current_state)]
print("Current score: ", current_score)
print("Hamming score: ", hamming_score)


def calculate_total_cost(current_score, distance_score):
    return current_score + distance_score


calculate_total_cost(current_score, hamming_score)

state_A = (1, 2, 3, 4, 5, 6, 0, 7, 8)
state_B = (1, 2, 3, 4, 5, 6, 7, 0, 8)
state_C = (1, 2, 3, 4, 5, 6, 7, 8, 0)

frontier = []

heapq.heappush(frontier, (8, state_A))
heapq.heappush(frontier, (3, state_B))
heapq.heappush(frontier, (5, state_C))

visited_states = set()

state_A = (1, 2, 3, 4, 5, 6, 0, 7, 8)

visited_states.add(state_A)

frontier = []
heapq.heappush(frontier, (10, state_A))


def find_smallest_priority(frontier, visited_states):
    while frontier:
        next_entry = heapq.heappop(frontier)
        if next_entry[1] not in visited_states:
            return next_entry


find_smallest_priority(frontier, visited_states)

state_A = (1, 2, 3, 4, 5, 6, 0, 7, 8)
state_B = (1, 2, 3, 4, 5, 6, 7, 0, 8)

visited_states = set({state_A})

frontier = []

heapq.heappush(frontier, (3, state_A))
heapq.heappush(frontier, (5, state_B))

assert find_smallest_priority(frontier, visited_states) == (5, state_B)

frontier = []

heapq.heappush(frontier, (3, state_A))
heapq.heappush(frontier, (5, state_B))

visited_states = set({state_A, state_B})

assert find_smallest_priority(frontier, visited_states) == None

frontier = []

heapq.heappush(frontier, (3, state_A))
heapq.heappush(frontier, (5, state_B))

visited_states = set()

assert find_smallest_priority(frontier, visited_states) == (3, state_A)

frontier = []
visited_states = set()

assert find_smallest_priority(frontier, visited_states) == None


def a_star(start_state, heuristic):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    visited_states = set()
    g_scores = {tuple(start_state): 0}
    frontier = []
    if heuristic == "hamming":
        score = calculate_hamming_distance(start_state)
    if heuristic == "manhattan":
        score = calculate_manhattan_distance(
            get_row_and_column(start_state), get_row_and_column(goal_state)
        )
    if is_solvable(start_state) == False:
        print("Invalid start state!")
        return
    else:
        heapq.heappush(frontier, (score, tuple(start_state)))
    while frontier:
        frontier_smallest_priority = find_smallest_priority(frontier, visited_states)
        if frontier_smallest_priority is not None:
            next_frontier = frontier_smallest_priority[1]
        else:
            print("Frontier empty!")
            return
        if next_frontier == tuple(goal_state):
            return (g_scores[next_frontier], len(visited_states))
        visited_states.add(next_frontier)
        next_states = generate_next_states(next_frontier)
        for state in next_states:
            if heuristic == "hamming":
                score = calculate_hamming_distance(state)
            if heuristic == "manhattan":
                score = calculate_manhattan_distance(
                    get_row_and_column(state), get_row_and_column(goal_state)
                )
            g_new = g_scores[next_frontier] + 1
            total_cost = calculate_total_cost(score, g_new)
            tuple_state = tuple(state)
            if tuple_state not in g_scores or g_new < g_scores[tuple_state]:
                g_scores.update({tuple_state: g_new})
                heapq.heappush(frontier, (total_cost, tuple_state))


result = a_star(
    [1, 2, 3, 4, 5, 6, 0, 7, 8],
    "hamming"
)
print(result)

test_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]

hamming_result = a_star(test_state, "hamming")
manhattan_result = a_star(test_state, "manhattan")

print(hamming_result[1])
print(manhattan_result[1])



test_set = set()

while len(test_set) < 100:
    test_set.add(tuple(generate_random_state()))

print(test_set)

start_time = time.perf_counter()

a_star(test_state, "hamming")

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(elapsed_time)