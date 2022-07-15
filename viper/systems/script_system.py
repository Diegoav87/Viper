from .system import System


class ScriptSystem(System):
    def check(self, entity):
        return len(entity.scripts) > 0

    def update_entity(self, entity):
        for script in entity.scripts:
            script.update()
