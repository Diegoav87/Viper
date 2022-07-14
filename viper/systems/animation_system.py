from .system import System


class AnimationSystem(System):
    def check(self, entity):
        return entity.animator is not None

    def update_entity(self, entity):
        entity.animator.update()
