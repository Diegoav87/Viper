import pygame


class InputController:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def check_input(self, entity):
        keys = pygame.key.get_pressed()

        if keys[self.right]:
            entity.intention.move_right = True
        else:
            entity.intention.move_right = False

        if keys[self.left]:
            entity.intention.move_left = True
        else:
            entity.intention.move_left = False

        if keys[self.up]:
            entity.intention.move_up = True
        else:
            entity.intention.move_up = False

        if keys[self.down]:
            entity.intention.move_down = True
        else:
            entity.intention.move_down = False

    def update(self, entity):
        self.check_input(entity)
