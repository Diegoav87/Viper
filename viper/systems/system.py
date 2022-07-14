class System:
    def __init__(self):
        pass

    def check(self, entity):
        return True

    def update(self, entities):
        for entity in entities:
            if self.check(entity):
                self.update_entity(entity)

    def update_entity(self, entity):
        pass
