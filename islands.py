# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# islands
# connected
# directoins, nsew
# 2d array
# returns (shape of solution)

# How can we find the extent of an island
# Either of our travels to find all of the nodes in an island

# How do I explore the larger set?
# Loop thorough and call a traversal if we find an alternative

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def island_counter(islands):
    num_islands = 0
    # iterate through the islands
    for y in range(0, len(islands)):
        for x in range(0, len(islands[y])):
            # if the island-node is part of an island and hasn't been visited
            if islands[y][x] == 1:
                # you've found an island, so increment
                num_islands += 1
                # BFT through the island-node's neighbors
                islands = visit_neighbors(x, y, islands)
    return num_islands


def visit_neighbors(x, y, islands):
    # NORTH
    if y > 0:  # if not at northern edge
        # and neighbor is an island-node
        if islands[y-1][x] == 1:
            # mark it visited by updating value to 0
            islands[y-1][x] = 0
            # and visit all it's neighbors
            islands = visit_neighbors(x, y-1, islands)

    # SOUTH
    if y < 4:
        if islands[y+1][x] == 1:
            islands[y+1][x] = 0
            islands = visit_neighbors(x, y+1, islands)
    # EAST
    if x < 4:
        if islands[y][x+1] == 1:
            islands[y][x+1] = 0
            islands = visit_neighbors(x+1, y, islands)
    # WEST
    if x > 0:
        if islands[y][x-1] == 1:
            islands[y][x-1] = 0
            islands = visit_neighbors(x-1, y, islands)
    return islands


result = island_counter(islands)

print(result)
