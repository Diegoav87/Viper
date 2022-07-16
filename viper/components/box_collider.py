import pygame


class BoxCollider:
    def __init__(self, transform, offset, size):
        self.transform = transform
        self.offset = pygame.math.Vector2(offset[0], offset[1])
        self.size = size
        self.rect = None
        self.set_rect()

    def set_rect(self):
        x = self.transform.rect.topleft[0] + self.offset.x
        y = self.transform.rect.topleft[1] + self.offset.y
        w = self.size[0]
        h = self.size[1]

        self.rect = pygame.Rect(x, y, w, h)

    def reset_position(self):
        self.transform.rect.x = self.rect.x - self.offset.x
        self.transform.rect.y = self.rect.y - self.offset.y
