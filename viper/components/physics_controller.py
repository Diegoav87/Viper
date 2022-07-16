import pygame


class PhysicsController:
    def __init__(self, speed):
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = speed

    def check_collision(self, entity, obstacles):
        for obstacle in obstacles:
            if obstacle.box_collider is not None:
                if obstacle.box_collider.rect.colliderect(entity.box_collider.rect):
                    if self.direction.x != 0 and self.direction.y == 0:
                        if self.direction.x > 0:
                            entity.box_collider.rect.right = obstacle.box_collider.rect.left
                        if self.direction.x < 0:
                            entity.box_collider.rect.left = obstacle.box_collider.rect.right
                    elif self.direction.x == 0 and self.direction.y != 0:
                        if self.direction.y < 0:
                            entity.box_collider.rect.top = obstacle.box_collider.rect.bottom
                        if self.direction.y > 0:
                            entity.box_collider.rect.bottom = obstacle.box_collider.rect.top
                    entity.box_collider.reset_position()

    def update(self, entity, obstacles):
        self.check_collision(entity, obstacles)
