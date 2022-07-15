import pygame


class PhysicsController:
    def __init__(self, speed):
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = speed

    # def move(self, entity):
    #     if entity.intention.move_right:
    #         self.direction.x = 1
    #         self.direction.y = 0
    #         entity.animator.state = 'right'
    #     elif entity.intention.move_left:
    #         self.direction.x = -1
    #         self.direction.y = 0
    #         entity.animator.state = 'left'
    #     elif entity.intention.move_up:
    #         self.direction.x = 0
    #         self.direction.y = -1
    #         entity.animator.state = 'up'
    #     elif entity.intention.move_down:
    #         self.direction.x = 0
    #         self.direction.y = 1
    #         entity.animator.state = 'down'
    #     else:
    #         self.direction.y = 0
    #         self.direction.x = 0

    #         if not "idle" in entity.animator.state:
    #             entity.animator.state += '_idle'

    #     entity.position.rect.x += self.direction.x * self.speed
    #     entity.position.rect.y += self.direction.y * self.speed

    #     if entity.box_collider is not None:
    #         entity.box_collider.set_rect()

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
