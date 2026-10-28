state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

state_tuple = tuple(state)

visited_states = set()

visited_states.add(state_tuple)

next_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

if tuple(next_state) in visited_states:
    print("Already visited!")
else:
    print("New state")

for x in visited_states:
    print(x)

state_A = (1, 2, 3, 4, 5, 6, 7, 0, 8)
state_B = (1, 2, 3, 4, 5, 6, 0, 7, 8)

g_scores = {state_A: 8}

print(g_scores[state_A])

new_g = 5

if state_A not in g_scores or new_g < g_scores[state_A]:
    g_scores[state_A] = new_g

print(g_scores[state_A])

current_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]

g_scores = {tuple(current_state): 4}

state = [1, 2, 3, 4, 5, 6, 8, 0, 7]


def get_row_and_column(state):
    coordinates = {}
    tiles_dimension = 3
    for index, tile in enumerate(state):
        coordinates[tile] = [index // tiles_dimension, index % tiles_dimension]
    return coordinates


get_row_and_column(state)

current_coordinates = get_row_and_column(state)
goal_coordinates = get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0])


def calculate_Manhattan_distance(current_coordinates, goal_coordinates):
    distance = {}
    for tile in current_coordinates:
        if tile == 0:
            continue
        distance[tile] = abs(
            current_coordinates[tile][0] - goal_coordinates[tile][0]
        ) + abs(current_coordinates[tile][1] - goal_coordinates[tile][1])
    return sum(distance.values())


calculate_Manhattan_distance(current_coordinates, goal_coordinates)

# tests
assert (
    calculate_Manhattan_distance(
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0]),
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0]),
    )
    == 0
)

assert (
    calculate_Manhattan_distance(
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 0, 8]),
        get_row_and_column([1, 2, 3, 4, 5, 6, 7, 8, 0]),
    )
    == 1
)

state_A = (1, 2, 3, 4, 5, 6, 0, 7, 8)
state_B = (1, 2, 3, 4, 5, 6, 7, 0, 8)
state_C = (1, 2, 3, 4, 5, 6, 7, 8, 0)

frontier = [(8, state_A), (3, state_B), (5, state_C)]

next_entry = min(frontier)
print(next_entry)


def find_smallest_priority(frontier):
    state_min = min(frontier)
    frontier.remove(state_min)
    return state_min


find_smallest_priority(frontier)

g_scores = {(1, 2, 3, 4, 5, 6, 0, 7, 8): 0}

print(g_scores.keys())
