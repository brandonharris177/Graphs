from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
retrace = []
traversal_graph = {}
visited = set()
travel_direction = ('w', 'e')
last_room = 'Not in graph'

while len(visited) < len(room_graph)-1:
    current_room = player.current_room.id
    exits = player.current_room.get_exits()
    
    if current_room not in visited:
        traversal_graph[current_room] = {}
        for each_exit in exits:
            traversal_graph[current_room][each_exit] = '?'
            visited.add(current_room)

    if last_room in traversal_graph:
        traversal_graph[current_room][travel_direction[1]] = last_room
        traversal_graph[last_room][travel_direction[0]] = current_room

    untravelded_directions = []
    for key, value in traversal_graph[current_room].items():
        if value == '?':
            untravelded_directions.append(key)

    while untravelded_directions == []:
        last_step = retrace.pop()
        if last_step == 's':
            travel_direction = ('n', 's')
        elif last_step == 'w':
            travel_direction = ('e', 'w')
        elif last_step == 'n':
            travel_direction = ('s', 'n')
        elif last_step == 'e':
            travel_direction = ('w', 'e')
        player.travel(travel_direction[0])
        traversal_path.append(travel_direction[0])
        current_room = player.current_room.id
        for key, value in traversal_graph[current_room].items():
            if value == '?':
                untravelded_directions.append(key)

    while travel_direction[0] not in untravelded_directions:
        next_travel = untravelded_directions[0] 
        if next_travel == 'n':
            travel_direction = ('n', 's')
        elif next_travel == 'e':
            travel_direction = ('e', 'w')
        elif next_travel == 's':
            travel_direction = ('s', 'n')
        elif next_travel == 'w':
            travel_direction = ('w', 'e')

    last_room = current_room
    player.travel(travel_direction[0])
    traversal_path.append(travel_direction[0])
    retrace.append(travel_direction[0])


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)


if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
