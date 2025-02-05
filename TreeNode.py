import heapq #importing heap from python library
import copy

# moveType, change in row, change in column
operators = [['up', -1, 0], ['down', 1, 0], ['left', 0, -1], ['right', 0, 1]]
    

class Node: 
    #default constructor for root node
    def __init__(self, state, parent = None):
        #list to represent 8puzzle board
        self.state = state
        self.parent = parent 
        self.length = len(state)
    
        
#find the position of the blank tile
#returns x (row) and y(column) for blank (0)
def find_zero(state):
    dim = len(state)
    #check rows
    for row in range(dim):
        #check column
        for column in range(dim):
            if state[row][column] == 0:
                return row, column
            
#come up with all possible node expansions from current blank tile position
def expand(node, operators):
    children = []
    #find position of blank tile; x = rows, y = columns
    x, y = find_zero(node.state)
    
    for moveType, change_x, change_y in operators:
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


