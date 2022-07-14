import pygame


class Camera:
    def __init__(self, screen, show_colliders):
        self.screen = screen
        self.show_colliders = show_colliders
        self.entity_to_track = None
        self.tilemap = None
        self.zoom_level = 1
        self.offset = pygame.math.Vector2(0, 0)

    def draw(self, layers):
        if self.entity_to_track is not None:
            self.offset.x = self.entity_to_track.position.rect.centerx - \
                self.screen.get_size()[0] // 2
            self.offset.y = self.entity_to_track.position.rect.centery - \
                self.screen.get_size()[1] // 2

        for layer in sorted(layers, key=lambda layer: layer.order):
            layer.draw(self.screen, self.offset, self.show_colliders)

    def update(self, layers):
        self.draw(layers)
