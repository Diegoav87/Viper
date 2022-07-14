class Layer:
    def __init__(self, name, order):
        self.name = name
        self.sprites = []
        self.order = order
        self.background = None
        self.background_rect = None

    def set_background(self, surface):
        self.background = surface
        self.background_rect = self.background.get_rect(topleft=(0, 0))

    def add(self, sprite):
        self.sprites.append(sprite)

    def draw(self, screen, offset, show_colliders):
        if self.background is not None:
            background_offset = self.background_rect.topleft - offset
            screen.blit(self.background, background_offset)

        for sprite in sorted(self.sprites, key=lambda sprite: sprite.position.rect.centery):
            sprite.draw(screen, offset, show_colliders)
