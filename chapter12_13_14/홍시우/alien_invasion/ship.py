import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """우주선을 관리하는 클래스"""

    def __init__(self, ai_game):
        """우주선을 초기화하고 시작 위치를 설정합니다"""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 우주선 이미지를 불러오고 사각형을 가져옵니다
        self.image = pygame.image.load('./alien_invasion/images/ship.bmp')
        self.rect  = self.image.get_rect()

        # 우주선 초기 위치는 화면 하단 중앙입니다
        self.rect.midbottom = self.screen_rect.midbottom

        # 우주선의 정확한 가로 위치 설정을 위해 부동 소수점 숫자를 저장합니다
        self.x = float(self.rect.x)

        # 움직임 플래그는 정지 상태로 시작합니다
        self.moving_right   = False
        self.moving_left    = False

    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치를 업데이트 합니다"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        """우주선을 현재 위치에 그립니다"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """우주선을 화면 하단 중앙으로 이동시킵니다"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)