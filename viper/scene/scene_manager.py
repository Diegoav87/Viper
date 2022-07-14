class SceneManager:
    def __init__(self):
        self.scenes = []

    def enter_scene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].on_enter()

    def exit_scene(self):
        if len(self.scenes) > 0:
            self.scenes[-1].on_exit()

    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update()

    def draw(self):
        if len(self.scenes) > 0:
            self.scenes[-1].draw()

    def push(self, scene):
        self.scenes.append(scene)
        self.enter_scene()

    def pop(self):
        self.scenes.pop()

    def set(self, scenes):
        while len(self.scenes) > 0:
            self.pop()

        for scene in scenes:
            self.push(scene)
