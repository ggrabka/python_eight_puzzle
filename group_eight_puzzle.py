import time
import heapq
import random
import statistics

puzzle_goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

GOAL_POSITIONS = {
    0: 0, 1: 1, 2: 2,
    3: 3, 4: 4, 5: 5,
    6: 6, 7: 7, 8: 8
}


class nodes:
    def __init__(self, puzzle_state, parent=None, g_cost=0, h_cost=0):
        self.puzzle_state = puzzle_state
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost


def idx_to_coords(idx):
    return idx // 3, idx % 3


def coords_to_idx(row, col):
    return row * 3 + col


def display_puzzle_state(puzzle_state):
    for r in range(3):
        row_display = ""
        for c in range(3):
            pos = coords_to_idx(r, c)
            tile_val = puzzle_state[pos]
            tile_char = "0" if tile_val == 0 else str(tile_val)
            row_display += tile_char
            if c < 2:
                row_display += "|"
        print(row_display)

        if r < 2:
            print("-----")


def generate_nodes(amount):
    manh_nodes = []
    hamm_nodes = []

    count = 0

    while count < amount:
        rand_state = random.sample(range(0, 9), 9)

        print(f"\n{'='*40}")
        print(f"generating puzzle #{count + 1}")
        print(f"{'='*40}")
        display_puzzle_state(rand_state)

        if not solvability_check(rand_state):
            print("\nnot solvable\nodd number of inversions\ngenerating new puzzle")
            continue

        print("\nsolvable\neven number of inversions")

        manh_node = nodes(
            puzzle_state=rand_state[:],
            parent=None,
            g_cost=0,
            h_cost=get_manh_value(rand_state)
        )

        hamm_node = nodes(
            puzzle_state=rand_state[:],
            parent=None,
            g_cost=0,
            h_cost=get_hamm_value(rand_state)
        )

        manh_nodes.append(manh_node)
        hamm_nodes.append(hamm_node)
        count += 1

    return manh_nodes, hamm_nodes


def solvability_check(start_state):
    inv_count = 0

    tiles_only = [val for val in start_state if val != 0]

    for i in range(len(tiles_only)):
        for j in range(i + 1, len(tiles_only)):
            if tiles_only[i] > tiles_only[j]:
                inv_count += 1

    return inv_count % 2 == 0


def get_manh_value(puzzle_state):
    total_dist = 0

    for pos in range(9):
        tile_val = puzzle_state[pos]

        if tile_val != 0:
            target_pos = GOAL_POSITIONS[tile_val]

            curr_r, curr_c = idx_to_coords(pos)
            target_r, target_c = idx_to_coords(target_pos)

            dist = abs(target_r - curr_r) + abs(target_c - curr_c)
            total_dist += dist

    return total_dist


def get_hamm_value(puzzle_state):
    wrong_count = 0

    for pos in range(9):
        tile_val = puzzle_state[pos]

        if tile_val != 0 and tile_val != puzzle_goal[pos]:
            wrong_count += 1

    return wrong_count


def get_next_nodes(node):
    child_states = []
    curr_state = node.puzzle_state

    empty_pos = curr_state.index(0)
    empty_r, empty_c = idx_to_coords(empty_pos)

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    for dr, dc in directions:
        adj_r = empty_r + dr
        adj_c = empty_c + dc

        if 0 <= adj_r < 3 and 0 <= adj_c < 3:
            adj_pos = coords_to_idx(adj_r, adj_c)

            next_state = curr_state[:]
            next_state[empty_pos], next_state[adj_pos] = next_state[adj_pos], next_state[empty_pos]

            child_states.append(next_state)

    return child_states


def solve_puzzle(node, heuristic_function):
    initial = node

    frontier = [initial]
    heapq.heapify(frontier)

    explored = set()

    exp_count = 0

    while frontier:
        curr = heapq.heappop(frontier)

        if curr.puzzle_state == puzzle_goal:
            return curr, exp_count

        state_key = tuple(curr.puzzle_state)
        if state_key in explored:
            continue

        child_states = get_next_nodes(curr)

        explored.add(state_key)
        exp_count += 1

        for child_state in child_states:
            child = nodes(
                puzzle_state=child_state,
                parent=curr,
                g_cost=curr.g_cost + 1,
                h_cost=heuristic_function(child_state)
            )
            heapq.heappush(frontier, child)

    return None, exp_count


if __name__ == "__main__":
    print("\n" + "-"*75)
    print("comparing heuristics")
    print("-"*75)

    manh_nodes, hamm_nodes = generate_nodes(100)

    results = {"manhattan": [], "hamming": []}

    for heur_name in ["manhattan", "hamming"]:
        print("\n" + "-"*75)
        print(f" running a* with {heur_name} heuristic")
        print("-"*75)

        exp_counts = []
        time_start = time.time()
        puzzle_num = 1

        if heur_name == "manhattan":
            node_list = manh_nodes
            heur_func = get_manh_value
        else:
            node_list = hamm_nodes
            heur_func = get_hamm_value

        for puzzle_node in node_list:
            solution, exp_count = solve_puzzle(puzzle_node, heur_func)
            exp_counts.append(exp_count)
            print(f" puzzle {puzzle_num:3d} solved ({exp_count:5d} nodes expanded)")
            puzzle_num += 1

        time_total = time.time() - time_start
        exp_mean = statistics.mean(exp_counts)
        exp_stdev = statistics.stdev(exp_counts)

        results[heur_name] = {
            "mean_nodes": exp_mean,
            "stdev_nodes": exp_stdev,
            "total_time": time_total
        }

        print(f"\n total time: {time_total:.2f}s")
        print(f" average nodes expanded: {exp_mean:.2f}")

    print("\n" + "-"*75)
    print("results")
    print("-"*75)
    print(f"| {'heuristic':<15} | {'mean nodes':<15} | {'standard dev':<15} | {'total time in s':<15} |")
    print("-"*75)

    for key, val in results.items():
        print(f"| {key:<15} | {val['mean_nodes']:<15.2f} | {val['stdev_nodes']:<15.2f} | {val['total_time']:<15.2f} |")

    print("-"*75)

    manh_mean = results["manhattan"]["mean_nodes"]
    hamm_mean = results["hamming"]["mean_nodes"]
    improvement = ((hamm_mean - manh_mean) / hamm_mean) * 100

    print(f"manhattan heuristic reduced node expansions by {improvement:.1f}%")
    print("\n" + "-"*75)
