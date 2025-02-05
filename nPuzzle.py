import TreeNode

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
          5, 4, 3]

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
    #queue of nodes
    nodes = []
    #dont want to visit same puzzle state more than once, using a set to avoid duplicates
    visited_set = set()
    nodes.append(TreeNode.Node(puzzle))
    
    #debug set max limit 
    max_limit = 5;

    #uniform cost search
    if queueing_function == 1:
        while len(nodes) != 0 or len(nodes) < max_limit:
            node = nodes.pop()
            new_nodes = TreeNode.expand(node, TreeNode.operators);
            visited_set.add(node);
            print(f"Number of nodes visited: {len(visited_set)}")
            # check if we have already seen/visited this node state
            for i in new_nodes:
                if i not in visited_set:
                    nodes.append(i)
                    print_puzzle(i.state)
                if is_goal_state(i.state):
                    return
                




#check if current state matches goal state
def is_goal_state(state):
    return state == goal_state

main()