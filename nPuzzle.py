import TreeNode
from TreeNode import add_to_set
from TreeNode import check_in_set
import heapq as hq
# class Puzzle:
#     def __init__(self, initial_state, goal_state):
#         self.initial_state = initial_state
#         self.goal_state = goal_state

# copied the menu from the sample code provided in the example project
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]

veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

oh_boy = [[8, 7, 1],
          [6, 0, 2],
          [5, 4, 3]]

#found impossible state from a google search
impossible = [[8, 1, 2],
              [0, 4, 3],
              [7, 6, 5]]

goal_state = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]


# from sample code provided in example
def init_default_puzzle_mode():
    selected_difficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Oh Boy' selected.")
        return oh_boy
    if selected_difficulty == "5":
        print("Difficulty of 'Impossible' selected.")
        return impossible
    
# taken from sample code provided in example report
def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                       "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1": 
        general_search(puzzle, 1)
    if algorithm == "2":
        general_search(puzzle, 2)
    if algorithm == '3':
        general_search(puzzle, 3)
    
# taken from sample code provided in example
def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')


# main function taken from sample code provided in the example project
def main():
    puzzle_mode = input( "Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
       select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print ( 
            "Enter your puzzle, using a zero to represent the blank. " + "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " + "the numbers with a space. RET only when finished." + '\n'
            )
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()
        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])
        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)
    return

#my code
def general_search(puzzle, queueing_function):
    print_puzzle(puzzle)
    #queue of nodes
    q = []
    #dont want to visit same puzzle state more than once, using a set to avoid duplicates
    visited_set = []
    hq.heappush(q, (0, TreeNode.Node(puzzle)))

    #uniform cost search
    if queueing_function == 1:
        #print_puzzle(puzzle)
        while len(q) != 0:
            cost, node = hq.heappop(q)
            #print_puzzle(node.state)
            if visited_set and check_in_set(visited_set, node):
                print("node = ", node.depth, " seen ... continue ...");
                continue;
            new_nodes = TreeNode.expand(node, TreeNode.operators)
            add_to_set(visited_set, node)
            print(f"Number of nodes visited: {len(visited_set)}, nodes_to_visit = {len(q)}")
            # check if we have already seen/visited this node state
            for i in new_nodes:
                if not check_in_set(visited_set, i):
                    hq.heappush(q, (0, i))
                    print_puzzle(i.state)
                if is_goal_state(i.state):
                    print (f"Solution depth: {i.depth}")
                    return
                
    #misplaced_tile
    if queueing_function == 2:
        #print_puzzle(puzzle)
        while len(q) != 0:
            cost, node = hq.heappop(q)
            children = TreeNode.expand(node, TreeNode.operators)
        for i in children:
            i.cost = misplaced_tile_heuristic(i.state)
            if is_goal_state(i.state):
                print_puzzle(i.state)
                print (f"Solution depth: {i.depth}")
                return
        hq.heappush(q, (0, find_least_cost(children)))

def find_least_cost(children):
    cost = -1
    node = None
    for i in children:
        if cost == -1 or i.cost < cost:
            cost = i.cost
            node = i
    print ("find_least...")
    print_puzzle(node.state)
    return node

def misplaced_tile_heuristic(puzzle):
    dim = len(puzzle)
    misplaced_tiles = 0
    #check rows
    for row in range(dim):
        #check column
        for column in range(dim):
            if puzzle[row][column] != goal_state[row][column]:
                misplaced_tiles += 1
    print_puzzle(puzzle)
    print(f"cost = {misplaced_tiles}")
    return misplaced_tiles

#def manhattan_distance_heuristic(puzzle):
    #tbd

#check if current state matches goal state
def is_goal_state(state):
    return state == goal_state


main()