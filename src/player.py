class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
        else:
            if direction == 'n':
                direction = 'north, '
                message = 'take a step and hit a brick wall. Try again.'
            elif direction == 'e':
                direction = 'east, '
                message = 'see glowing eyes in the distance, and decide that may not be a good idea. Try again.'
            elif direction == 's':
                direction = 'south '
                message = 'and nearly fall straight down a cliff. Be careful!'
            elif direction == 'w':
                direction = 'west '
                message = f'and Siri warns you this is not the right way, {self.name}. Try again.'
            print(f"\nYou turn {direction}{message}\n-------------------------------\n-------------------------------")

