from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].connections['n'] = room['foyer']
room['foyer'].connections['s'] = room['outside']
room['foyer'].connections['n'] = room['overlook']
room['foyer'].connections['e'] = room['narrow']
room['overlook'].connections['s'] = room['foyer']
room['narrow'].connections['w'] = room['foyer']
room['narrow'].connections['n'] = room['treasure']
room['treasure'].connections['s'] = room['narrow']

# Main
# Welcome message
# print('Welcome to the game! What should we call you?')
# user = input('Name:')

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
        
print('-----------------------------------------------\nWelcome to the game! What should we call you?\n-----------------------------------------------')
player = Player(input('Name:'), room['outside'])
print(f'\n===============================================\n{player.name}, your jorney begins {player.current_room.name}\n===============================================\n')

user_is_playing = True

while user_is_playing:
    print('\n')
    for line in textwrap.wrap(player.current_room.description):
        print(line)

    user_input = input('\nWhich direction would you like to go?\n Type n,s,e, or w to move\n Type q to quit\nYour selection:  ')
    
    if user_input in ['n', 'e', 's', 'w']:
        player.move(user_input)
    elif user_input == 'q':
        print('\nThank you for playing!\nGoodbye!\n-----------------------------------------------')
        user_is_playing = False
    elif user_input != ['n', 'e', 's', 'w', 'q']:
        print(f'\n{player.name}, {user_input} is not a direction.\n')
