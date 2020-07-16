        # print(untravelded_directions)
        last_step = traversal_path[backward_steps]
        # print("backward_steps", traversal_path[backward_steps], "number", backward_steps)
        # print(last_step)
        if last_step == 's':
            travel_direction = ('n', 's')
        elif last_step == 'w':
            travel_direction = ('e', 'w')
        elif last_step == 'n':
            travel_direction = ('s', 'n')
        elif last_step == 'e':
            travel_direction = ('w', 'e')
        player.travel(travel_direction[0])
        # print("traveled 1", travel_direction[0])
        traversal_path.append(travel_direction[0])
        # print("travel path", traversal_path)
        current_room = player.current_room.id
        # print("curent room", current_room)
        for key, value in traversal_graph[current_room].items():
            if value == '?':
                untravelded_directions.append(key)
                # print("untraveled", untravelded_directions)
        backward_steps = backward_steps-2