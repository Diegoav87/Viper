import os
import pygame


def get_folder_names(path):
    for root, dirs, files in os.walk(path):
        return dirs


def import_folder(path):
    frames = []

    for _, __, files in os.walk(path):
        for file in sorted(files, key=len):
            full_path = path + '/' + file
            image_surf = pygame.image.load(full_path).convert_alpha()
            frames.append(image_surf)

    return frames


def slice_spritesheet(path, tile_size_x, tile_size_y):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size_x)
    tile_num_y = int(surface.get_size()[1] / tile_size_y)

    cutted_tiles = []

    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size_x
            y = row * tile_size_y
            new_surface = pygame.Surface((tile_size_x, tile_size_y))
            new_surface.set_colorkey((0, 0, 0))
            new_surface.blit(surface, (0, 0), pygame.Rect(
                x, y, tile_size_x, tile_size_y))
            cutted_tiles.append(new_surface)

    return cutted_tiles
