import pygame
from settings import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.x, self.y, = x, y
        self.text = text
        self.rect = self.image.get_rect()
        
        if (self.text != "Empty"):
            self.font = pygame.font.SysFont("Consolas", TILE_TEXTSIZE)
            font_surface = self.font.render(self.text, True, BLACK)
            self.image.fill(WHITE)
            self.font_size = self.font.size(self.text)
            draw_x = (TILESIZE / 2) - self.font_size[0] / 2
            draw_y = (TILESIZE / 2) - self.font_size[1] / 2
            self.image.blit(font_surface, (draw_x, draw_y))
        else:
            self.image.fill(BGCOLOR)
        
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        
    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom
    
    # Verifica se o Tile tá dentro da Grid
    def right(self):
        return self.rect.x + TILESIZE < GAMESIZE * TILESIZE
    
    def left(self):
        return self.rect.x - TILESIZE >= 0
    
    def up(self):
        return self.rect.y - TILESIZE >= 0
    
    def down(self):
        return self.rect.y + TILESIZE < GAMESIZE * TILESIZE
    
class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
        
    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 35)
        text = font.render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))
        
class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.color, self.text_color = color, text_color
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.text = text
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self. y, self.width, self.height))
        font = pygame.font.SysFont("Consolas", 35)
        text = font.render(self.text, True, self.text_color)
        self.font_size = font.size(self.text)
        draw_x = self.x + (self.width / 2) - self.font_size[0] / 2
        draw_y = self.y + (self.height / 2) - self.font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))
        
    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height