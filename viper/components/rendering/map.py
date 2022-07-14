from csv import reader


class Map:
    def __init__(self, csv_path, name):
        self.csv_path = csv_path
        self.name = name
        self.map = self.import_csv_layout(self.csv_path)

    def import_csv_layout(self, path):
        terrain_map = []

        with open(path) as level_map:
            layout = reader(level_map, delimiter=',')

            for row in layout:
                terrain_map.append(list(row))
            return terrain_map
