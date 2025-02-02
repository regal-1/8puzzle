import TreeNode
import heapq 

# Below are some built-in puzzles to allow quick testing.
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

#found this from a google search
impossible = [[8, 1, 2],
              [0, 4, 3],
              [7, 6, 5]]

eight_goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]
def main():
    puzzle_mode = input ( "Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
       ()
    # TBD! select_and_init_algorithm(init_default_puzzle_mode())
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
            # TBD! select_and_init_algorithm(user_puzzle)
    return

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
    
def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
        print('\n')

print ("main")
main