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
bread_crumbs = []
map = {}
visited = set()
last_room = ""

compass = {
    'n': ('n', 's'),
    'e': ('e', 'w'),
    's': ('s', 'n'),
    'w': ('w', 'e')
}

travel_direction = compass['n']

def untraveled(current_room):
    untraveled_list = []
    for key, value in map[current_room].items():
        if value == '?':
            untraveled_list.append(key)
    return untraveled_list

while len(visited) < len(room_graph)-1:
    current_room = player.current_room.id
    exits = player.current_room.get_exits()

    if current_room not in visited:
        map[current_room] = {}
        for each_exit in exits:
            map[current_room][each_exit] = '?'
            visited.add(current_room)

    if last_room in map:
        map[current_room][travel_direction[1]] = last_room
        map[last_room][travel_direction[0]] = current_room

    untraveled_directions = untraveled(current_room)

    while untraveled_directions == []:
        last_step = bread_crumbs.pop()
        travel_direction = compass[last_step]
        player.travel(travel_direction[0])
        traversal_path.append(travel_direction[0])
        current_room = player.current_room.id
        untraveled_directions = untraveled(current_room)

    while travel_direction[0] not in untraveled_directions:
        next_travel = untraveled_directions[0] 
        travel_direction = compass[next_travel]

    last_room = current_room
    player.travel(travel_direction[0])
    traversal_path.append(travel_direction[0])
    bread_crumbs.append(travel_direction[1])


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
