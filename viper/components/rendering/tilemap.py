class Tilemap:
    def __init__(self, order_in_layer):
        self.tiles = []
        self.order_in_layer = order_in_layer

    def add_tile(self, tile):
        self.tiles.append(tile)
