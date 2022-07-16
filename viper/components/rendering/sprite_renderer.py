import pygame


class SpriteRenderer:
    def __init__(self, image, order_in_layer):
        super().__init__()
        self.image = image
        self.flip_x = False
        self.flip_y = False
        self.order_in_layer = order_in_layer
        self.transform = None
        self.box_collider = None

    def draw_collider(self, screen, offset):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.box_collider.rect.x - offset.x,
                         self.box_collider.rect.y - offset.y, self.box_collider.rect.width, self.box_collider.rect.height), 1)

    def draw(self, screen, offset):
        offset_position = self.transform.rect.topleft - offset
        flipped_image = pygame.transform.flip(
            self.image, self.flip_x, self.flip_y)
        scaled_image = pygame.transform.scale(
            flipped_image, (self.transform.scale.x * self.transform.rect.width, self.transform.scale.y * self.transform.rect.height))
        rotated_image = pygame.transform.rotate(
            scaled_image, self.transform.rotation)
        screen.blit(rotated_image, offset_position)
