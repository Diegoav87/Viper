from .system import System


class InputSystem(System):
    def check(self, entity):
        return entity.input is not None

    def update_entity(self, entity):
        entity.input.update(entity)
