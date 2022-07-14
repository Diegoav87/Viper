from .system import System


class CameraSystem(System):
    def check(self, entity):
        return entity.camera is not None

    def update(self, entities, layers):
        for entity in entities:
            if self.check(entity):
                self.update_entity(entity, layers)

    def update_entity(self, entity, layers):
        entity.camera.update(layers)
