import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """함대 내 한 명의 외계인을 나타내는 클래스"""

    def __init__(self, ai_settings, screen):
        """외계인을 초기화하고 시작 위치를 설정합니다"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 외계인 이미지를 로드하고 해당 이미지의 rect 속성을 설정합니다
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 화면 왼쪽 상단에서 새로운 외계인을 하나씩 시작하세요
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 외계인의 정확한 위치를 저장하세요
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """외계인이 화면 가장자리에 있으면 True를 반환합니다"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """외계인을 오른쪽 또는 왼쪽으로 이동합니다"""
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """현재 위치에 외계인을 그립니다"""
        self.screen.blit(self.image, self.rect)
