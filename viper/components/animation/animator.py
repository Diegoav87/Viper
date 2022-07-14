class Animator:
    def __init__(self, initial_state):
        self.state = initial_state
        self.animations = {}
        self.sprite_renderer = None

    def add(self, state, animation):
        self.animations[state] = animation

    def update(self):
        self.animations[self.state].update(self.sprite_renderer)
