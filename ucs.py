import heapq #importing heap from python library

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    #check if current state matches goal state
    def is_goal_state(self, state):
        return state == self.goal_state
    

class Node: 
    #default constructor for root node
    def __init__(self, state, parent = None):
        #list to represent 8puzzle board
        self.state = state
        self.parent = parent 
    
        

#find the position of the blank tile
#returns x (row) and y(column) for blank (0)
def find_zero(state):
    #check rows
    for x in range(3):
        #check column
        for y in range(3):
            if state[x][y] == 0:
                return x, y
            
#come up with all possible node expansions from current blank tile position
def expand(node, operators):
    children = []
    #find position of blank tile
    x, y = find_zero(node.state)

    for change_x, change_y in operators:
        new_x, new_y = x + change_x, y + change_y
        #make sure move does not go outside the puzzle boundary
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(node.state)
            #swap the tiles
            tile1 = new_state[x][y]
            tile2 = new_state[new_x][new_y]
            new_state[new_x][new_y] = tile1
            new_state[x][y] = tile2
            children.append(Node(new_state, node))

    return children


