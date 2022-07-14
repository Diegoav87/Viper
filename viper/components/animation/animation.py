class Animation:
    def __init__(self, frames, interval):
        self.frames = frames
        self.frame_index = 0
        self.interval = interval

    def update(self, sprite_renderer):
        self.frame_index += self.interval

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        sprite_renderer.image = self.frames[int(self.frame_index)]
