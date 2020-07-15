"""
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west. For example:

island_counter(islands) # returns 4

Describe the problem in terms of graphs
nodes: 1s
edge: connected n/s/w/e

islands: connected components

Build our graph or just define getNeighbors()


visited = set((0, 1))


Plan
## Iterate through the matrix
### When we see a 1, if it's not been visited
#### Increment our islands counter
#### run a traversal
##### mark things as visited

"""

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# stepNorth = row > 0 

def get_neighbors(node, matrix):
    row, col = node

    neighbors = []

    stepNorth = stepSouth = stepWest = stepEast = False
    ## take a step north
    if row > 0:
        stepNorth = row - 1
    ## take a step south
    if row < len(matrix) - 1:
        stepSouth = row + 1
    ## take a step east
    if col < len(matrix[row]) - 1:
        stepEast = col + 1
    ## take a step west
    if col > 0:
        stepWest = col - 1

    if stepNorth is not False and matrix[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))

    if stepSouth is not False and matrix[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))

    if stepEast is not False and matrix[row][stepEast] == 1:
        neighbors.append((row, stepEast))

    if stepWest is not False and matrix[row][stepWest] == 1:
        neighbors.append((row, stepWest))

    return neighbors


def dft_recursive(node, visited, matrix):
    ### if node not visited
    if node not in visited:
        ### add to visited
        visited.add(node)
        
        ### get neighbors
        neighbors = get_neighbors(node, matrix)
        ### for each neighbor
        for neighbor in neighbors:
        #### recurse
            dft_recursive(neighbor, visited, matrix)

def islands_counter(isles):
    visited = set()
    number_islands = 0

## Iterate through the matrix
    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col)
### When we see a 1, if it's not been visited
            if node not in visited and isles[row][col] == 1:
            #### Increment our islands counter
                number_islands += 1
            #### run a traversal
                dft_recursive(node, visited, isles)

    return number_islands

print(islands_counter(islands))
print(islands_counter(big_islands))