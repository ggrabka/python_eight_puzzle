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

g_scores = {
    tuple(current_state): 4
}

next_states = generate_next_states(current_state)
