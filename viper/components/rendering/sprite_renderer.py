import pygame


class SpriteRenderer:
    def __init__(self, image, order_in_layer):
        super().__init__()
        self.image = image
        self.flip_x = False
        self.flip_y = False
        self.order_in_layer = order_in_layer
        self.position = None
        self.box_collider = None

    def draw_collider(self, screen, offset):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.box_collider.rect.x - offset.x,
                         self.box_collider.rect.y - offset.y, self.box_collider.rect.width, self.box_collider.rect.height), 1)

    def draw(self, screen, offset):
        offset_rect = self.position.rect.topleft - offset
        screen.blit(self.image, offset_rect)
