class Room:
    ## Default params because only one selection is made at a time
    def __init__(self, name, description, items=[], n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.connections = {
            'n' : n_to,
            's' : e_to,
            'e' : s_to,
            'w' : w_to
        }
        self.items = items
