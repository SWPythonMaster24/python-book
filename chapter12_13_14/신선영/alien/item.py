import pygame
from pygame.sprite import Sprite
from random import randint

class Item(Sprite):
    def __init__(self, ai_settings, screen):
        super(Item, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/item.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx + randint(-400, 400)
        self.rect.bottom = self.screen_rect.bottom
