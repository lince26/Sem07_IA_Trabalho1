import pygame
import random
import time
from settings import *
from sprite import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        
    def create_game(self):
        grid = []
        number = 1
        for x in range(GAMESIZE):
            grid.append([])
            for y in range (GAMESIZE):
                grid[x].append(number)
                number += 1
        
        grid[-1][-1] = 0
        return grid
    
    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if (tile != 0):
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                else:
                    self.tiles[row].append(Tile(self, col, row, "Empty"))
        
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        
        # O que vai ser mudado
        self.tiles_grid = self.create_game()
        # Vai ter o resultado
        self.tiles_grid_completed = self.create_game()
        
        self.draw_tiles()
    
    def run(self):
        self.playing = True
        while (self.playing):
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        self.all_sprites.update()
    
    def draw_grid(self):
        for row in range(-1, GAMESIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGRAY, (row, 0), (row, GAMESIZE * TILESIZE))
        
        for col in range(-1, GAMESIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGRAY, (0, col), (GAMESIZE * TILESIZE, col))
    
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit(0)
                
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row, tiles in enumerate(self.tiles):
                    for col, tile in enumerate(tiles):
                        if (tile.click(mouse_x, mouse_y)):
                            if (tile.right() and self.tiles_grid[row][col+1] == 0):
                                self.tiles_grid[row][col], self.tiles_grid[row][col+1] = self.tiles_grid[row][col+1], self.tiles_grid[row][col]
                            
                            if (tile.left() and self.tiles_grid[row][col-1] == 0):
                                self.tiles_grid[row][col], self.tiles_grid[row][col-1] = self.tiles_grid[row][col-1], self.tiles_grid[row][col]
                                
                            if (tile.up() and self.tiles_grid[row-1][col] == 0):
                                self.tiles_grid[row][col], self.tiles_grid[row-1][col] = self.tiles_grid[row-1][col], self.tiles_grid[row][col]
                                
                            if (tile.down() and self.tiles_grid[row+1][col] == 0):
                                self.tiles_grid[row][col], self.tiles_grid[row+1][col] = self.tiles_grid[row+1][col], self.tiles_grid[row][col]
                                
                            self.draw_tiles()
    

game = Game()
while (True):
    game.new()
    game.run()