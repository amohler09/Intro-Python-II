class Room:
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.connections = {
            'n' : n_to,
            's' : e_to,
            'e' : s_to,
            'w' : w_to
        }
       