from .system import System


class PhysicsSystem(System):
    def check(self, entity):
        return entity.physics_controller is not None and entity.transform is not None

    def update(self, entities):
        obstacles = []
        for entity in entities:
            if entity.tag == 'Obstacle':
                obstacles.append(entity)

        for entity in entities:
            if self.check(entity):
                self.update_entity(entity, obstacles)

    def update_entity(self, entity, obstacles):
        entity.physics_controller.update(entity, obstacles)
