"""8-puzzle heuristic search: Hamming versus Manhattan distance."""

import heapq
import random
import statistics
import time

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


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
        new_list = list(state)
        zero_value_index = new_list.index(0)
        new_list[zero_value_index], new_list[move] = (
            new_list[move], new_list[zero_value_index]
        )
        move_collection.append(new_list)
    return move_collection


def count_inversions(state):
    inversion_count = 0
    for index, current_state in enumerate(state):
        if current_state == 0:
            continue
        for x in state[index + 1:]:
            if x == 0:
                continue
            if current_state > x:
                inversion_count += 1
    return inversion_count


def is_solvable(state):
    inversion_count = count_inversions(state)
    return inversion_count % 2 == 0


def generate_random_state():
    while True:
        numbers = list(range(9))
        random.shuffle(numbers)
        if is_solvable(numbers):
            return numbers


def calculate_hamming_distance(state):
    misplaced_tiles = 0
    for index, tile in enumerate(state):
        if tile != GOAL_STATE[index] and tile != 0:
            misplaced_tiles += 1
    return misplaced_tiles


def get_row_and_column(state):
    coordinates = {}
    tiles_dimension = 3
    for index, tile in enumerate(state):
        coordinates[tile] = [index // tiles_dimension, index % tiles_dimension]
    return coordinates


def calculate_manhattan_distance(current_coordinates, goal_coordinates):
    distance = {}
    for tile in current_coordinates:
        if tile == 0:
            continue
        distance[tile] = abs(
            current_coordinates[tile][0] - goal_coordinates[tile][0]
        ) + abs(current_coordinates[tile][1] - goal_coordinates[tile][1])
    return sum(distance.values())


def calculate_total_cost(current_score, distance_score):
    return current_score + distance_score


def find_smallest_priority(frontier, visited_states):
    while frontier:
        next_entry = heapq.heappop(frontier)
        if next_entry[1] not in visited_states:
            return next_entry
    return None


def a_star(start_state, heuristic):
    """Return (solution length, expanded states), or None if unsolvable."""
    if not is_solvable(start_state):
        return None
    if heuristic not in ("hamming", "manhattan"):
        raise ValueError("heuristic must be 'hamming' or 'manhattan'")

    visited_states = set()
    g_scores = {tuple(start_state): 0}
    frontier = []
    goal_coordinates = get_row_and_column(GOAL_STATE)

    if heuristic == "hamming":
        score = calculate_hamming_distance(start_state)
    else:
        score = calculate_manhattan_distance(
            get_row_and_column(start_state), goal_coordinates
        )
    heapq.heappush(frontier, (score, tuple(start_state)))

    while frontier:
        frontier_smallest_priority = find_smallest_priority(frontier, visited_states)
        if frontier_smallest_priority is None:
            return None

        next_frontier = frontier_smallest_priority[1]
        if next_frontier == GOAL_STATE:
            return g_scores[next_frontier], len(visited_states)

        visited_states.add(next_frontier)
        next_states = generate_next_states(next_frontier)
        for state in next_states:
            if heuristic == "hamming":
                score = calculate_hamming_distance(state)
            else:
                score = calculate_manhattan_distance(
                    get_row_and_column(state), goal_coordinates
                )
            g_new = g_scores[next_frontier] + 1
            total_cost = calculate_total_cost(score, g_new)
            tuple_state = tuple(state)
            if tuple_state not in g_scores or g_new < g_scores[tuple_state]:
                g_scores[tuple_state] = g_new
                heapq.heappush(frontier, (total_cost, tuple_state))
    return None


def solveEightPuzzle(test_states, heuristic):
    """Collect (solution length, expanded nodes, elapsed seconds) per state."""
    results = []
    for state in test_states:
        start_time = time.perf_counter()
        solution_length, expanded_nodes = a_star(state, heuristic)
        elapsed_time = time.perf_counter() - start_time
        results.append((solution_length, expanded_nodes, elapsed_time))
    return results


def calculate_statistics(results):
    expanded_nodes = [result[1] for result in results]
    execution_times = [result[2] for result in results]
    return {
        "mean_expanded_nodes": statistics.mean(expanded_nodes),
        "std_expanded_nodes": statistics.stdev(expanded_nodes),
        "mean_execution_time": statistics.mean(execution_times),
        "std_execution_time": statistics.stdev(execution_times),
    }


def run_tests():
    """Quick correctness and helper-function regression checks."""
    assert len(generate_next_states([1, 2, 3, 4, 5, 6, 0, 7, 8])) == 2
    assert len(generate_next_states([1, 2, 3, 4, 0, 5, 6, 7, 8])) == 4
    assert len(generate_next_states([1, 0, 2, 3, 4, 5, 6, 7, 8])) == 3
    state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    original = state.copy()
    successors = generate_next_states(state)
    assert state == original
    assert all(sorted(successor) == list(range(9)) for successor in successors)
    assert successors == generate_next_states(state)

    assert count_inversions(GOAL_STATE) == 0
    assert count_inversions([2, 1, 3, 4, 5, 6, 8, 7, 0]) == 2
    assert count_inversions([3, 2, 1, 4, 5, 6, 7, 8, 0]) == 3
    assert count_inversions([8, 7, 6, 5, 4, 3, 2, 1, 0]) == 28
    assert is_solvable(GOAL_STATE)
    assert not is_solvable([1, 2, 3, 4, 5, 6, 8, 7, 0])
    assert is_solvable([2, 1, 3, 4, 5, 6, 8, 7, 0])

    for state, expected in [
        (GOAL_STATE, 0),
        ([1, 2, 3, 4, 5, 6, 7, 0, 8], 1),
        ([1, 2, 3, 4, 5, 6, 0, 7, 8], 2),
    ]:
        assert calculate_hamming_distance(state) == expected
        assert calculate_manhattan_distance(
            get_row_and_column(state), get_row_and_column(GOAL_STATE)
        ) == expected
        for heuristic in ("hamming", "manhattan"):
            assert a_star(state, heuristic)[0] == expected

    assert calculate_hamming_distance([1, 2, 3, 4, 0, 6, 7, 5, 8]) == 2
    assert a_star([1, 2, 3, 5, 0, 6, 4, 7, 8], "hamming")[0] == 4
    assert a_star([1, 2, 3, 5, 0, 6, 4, 7, 8], "manhattan")[0] == 4

    state_a = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    state_b = (1, 2, 3, 4, 5, 6, 7, 0, 8)
    for visited, expected in [({state_a}, (5, state_b)),
                              ({state_a, state_b}, None),
                              (set(), (3, state_a))]:
        frontier = [(3, state_a), (5, state_b)]
        heapq.heapify(frontier)
        assert find_smallest_priority(frontier, visited) == expected
    assert find_smallest_priority([], set()) is None


def main():
    run_tests()
    test_set = set()
    while len(test_set) < 100:
        test_set.add(tuple(generate_random_state()))
    test_states = list(test_set)

    hamming_results = solveEightPuzzle(test_states, "hamming")
    manhattan_results = solveEightPuzzle(test_states, "manhattan")
    assert len(hamming_results) == len(manhattan_results) == 100
    for hamming, manhattan in zip(hamming_results, manhattan_results):
        assert hamming[0] == manhattan[0]

    print("Hamming:", calculate_statistics(hamming_results))
    print("Manhattan:", calculate_statistics(manhattan_results))


if __name__ == "__main__":
    main()
