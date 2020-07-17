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
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# create a dictionary/parent dictionary
visited = {}

navi = {"n": "s", "s": "n", "e": "w", "w":"e" } # navigate back from where i came

revPath = []

# ssave and show direction
visited[player.current_room.id] = player.current_room.get_exits() 

while len(visited) < len(room_graph): 
    print("Current Room:", player.current_room.id)
    if player.current_room.id not in visited: # In a new unvisited room
        revDirection = revPath[-1] # to back track where i came from
        visited[player.current_room.id] = player.current_room.get_exits() # Save current room in visited
        visited[player.current_room.id].remove(revDirection) #remove the previous room from
    
    elif len(visited[player.current_room.id]) == 0: #if there are no more exits inthe room
        revDirection = revPath.pop() # to back track where i came from and reemove from revPath
        traversal_path.append(revDirection) # save path
        player.travel(revDirection) # go back!
    
    elif len(visited[player.current_room.id]) > 0: # if there are more exits to explore
        direction = visited[player.current_room.id].pop()
        revPath.append(navi[direction]) #set revPath for current room
        traversal_path.append(direction) # set path for current direction
        player.travel(direction) # move forward!


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

## 1003 moves