import pygame


class Transform:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.rotation = 0
        self.scale = pygame.math.Vector2(1, 1)
        self.initial = pygame.Rect(x, y, w, h)
