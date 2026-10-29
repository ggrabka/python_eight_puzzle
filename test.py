import heapq
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

board = [1, 2, 3, 4, 0, 5, 7, 8, 6]


if 0 in board:
    print("0 is in the board")
if 9 not in board:
    print("9 is absent")
for x in board:
    print(x)
for x in board:
    if x == 0:
        continue
    print(x)

board = [1, 2, 3, 4, 0, 5, 7, 8, 6]


board = [1, 2, 3, 4, 5, 0, 7, 8, 6]

empty_index = board.index(0)
print("index: ", empty_index)
right_tile_index = empty_index + 1
if empty_index // 3 != right_tile_index // 3:
    print("No tile to the right")
else:
    print(board[right_tile_index])

state = (1, 2, 3, 4, 0, 5, 7, 8, 6)

state_list = list(state)
print(state_list)
state_index_four = state_list[4]
state_index_five = state_list[5]
state_list[4] = state_index_five
state_list[5] = state_index_four

new_state = tuple(state_list)
print(state, new_state)

state_list = [1, 2, 3, 4, 0, 5, 7, 8, 6]
state_tuple = (1, 2, 3, 4, 0, 5, 7, 8, 6)

visited = {}

visited[state_tuple] = True
print(visited)

visited[tuple(state_list)] = True
print(visited)

state_a = (1, 2, 3, 4, 0, 5, 7, 8, 6)
state_b = (1, 2, 3, 4, 5, 0, 7, 8, 6)
state_c = (1, 2, 3, 4, 0, 5, 7, 8, 6)

visited = set()
visited.add(state_a)
visited.add(state_b)
visited.add(state_c)
print(visited)
print(len(visited))

if state_b in visited:
    print("state b is in visited")

visited = {1, 2, 3, 4, 5}
visited.remove(3)
print(visited)
visited.discard(3)

visited = {2, 4, 6, 8}

if 4 in visited:
    print("four is in visited")
if 5 not in visited:
    print("sorry, five is not in visited")
for x in visited:
    print(x)

scores = {"state_a": 0, "state_b": 1, "state_c": 2}

print("Print state_b of scores: ", scores["state_b"])

scores["state_c"] = 5

scores["state_d"] = 3

print(scores)


scores = {"state_a": 0, "state_b": 1, "state_c": 5}

costs = {(1, 2, 3, 4, 0, 5, 7, 8, 6): 4, (1, 2, 3, 4, 5, 0, 7, 8, 6): 5}

if 5 in costs.values():
    print("Costs found")
if (1, 2, 3, 4, 0, 5, 7, 8, 6) in costs:
    print("state found")


scores = {"state_a": 2, "state_b": 5, "state_c": 3}

for x in scores:
    print(x)
for x in scores.values():
    print(x)
for key, value in scores.items():
    print(key, "has a value ", value)

costs = {
    "state_a": 3,
    "state_b": 5
}

cost_a = costs.get("state_a")
cost_c = costs.get("state_c")
cost_b = costs["state_b"]
cost_c_100 = costs.get("state_c", 100)
print(cost_a)
print(cost_b)
print(cost_c)
print(cost_c_100)
print(costs)

state_a = (1, 2, 3, 4, 0, 5, 7, 8, 6)
state_b = (1, 2, 3, 4, 5, 0, 7, 8, 6)
state_c = (1, 2, 3, 4, 5, 6, 7, 8, 0)

visited = set()
g_scores = {}

visited.add(state_a)
visited.add(state_b)

g_scores[state_a] = 0
g_scores[state_b] = 1

if state_c not in visited:
    print("New state discovered")

state_a = (1, 2, 3)
state_b = (4, 5, 6)

visited = {state_a}

g_scores = {
    state_a: 0,
    state_b: 1
}

tiles = [1, 2, 3, 2, 4, 5]

tiles_tuple = tuple(tiles)
tiles_set = set(tiles)
unique_tiles = list(tiles_set)

print("tiles tuple: ", tiles_tuple)
print("tiles set: ", tiles_set)
print("tiles unique: ", unique_tiles)

print(len(tiles), len(tiles_set))

state = [1, 2, 3, 4, 0, 5, 7, 8, 6]

visited = set()
visited.add(tuple(state))

if tuple(state) in visited:
    print("Already visited")

state = [1, 2, 3, 4, 0, 5, 7, 8, 6]

successor = list(state)
print("successor: ", successor)
successor[4] = 5
successor[5] = 0

print("Original:", state)
print("Successor:", successor)

state = [1, 2, 3, 4, 0, 5, 7, 8, 6]
index_zero = state.index(0)

print("zero index", index_zero)

index_right = index_zero + 1
index_left = index_zero - 1

if(index_zero // 3 == index_right // 3):
    successor_right_state = list(state)
    successor_right_state[index_zero] = successor_right_state[index_right]
    successor_right_state[index_right] = 0
    successor_right_state = tuple(successor_right_state)

if(index_zero // 3 == index_left // 3):
    successor_left_state = list(state)
    successor_left_state[index_zero] = successor_left_state[index_left]
    successor_left_state[index_left] = 0
    successor_left_state = tuple(successor_left_state)



print(state)
print(successor_left_state)
print(successor_right_state)

state_A = (1, 2, 3, 4, 5, 6, 0, 7, 8)
state_B = (1, 2, 3, 4, 5, 6, 7, 0, 8)

frontier = []

heapq.heappush(frontier, (3, state_A))
heapq.heappush(frontier, (5, state_B))

smallest_frontier = heapq.heappop(frontier)

print(smallest_frontier[1])

g_scores = {(1, 2, 3, 4, 5, 6, 7, 0, 8) : 0,
            (1, 2, 3, 4, 5, 6, 7, 0, 8) : 2}

tuple_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)
g_new = 1

if tuple_state not in g_scores or g_new < g_scores[tuple_state]:
    g_scores.update({tuple_state: g_new})

print(g_scores)
