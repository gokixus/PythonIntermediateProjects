import pygame
import random

pygame.init()

win = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Tetris")

#block
grid_width = 20
grid_height = 25

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

#shapes
shapes = [
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 0], [0, 1, 1]],  # Z shpae
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[1, 1, 1], [1, 0, 0]],  # L shape
    [[1, 1, 1], [0, 0, 1]]   # J shape
]

class Tetris():
    def __init__(self):
        pass
        
    def new_shape():
        pass
    
    def rotate_shape():
        pass
    
    def create_grid():
        pass
    
    def draw_shape():
        pass
    
    def draw_grid():
        pass 
    
    def intersects():
        pass
    
    def remove_line():
        pass
    
    def freeze():
        pass
    
    def down():
        pass
    

    