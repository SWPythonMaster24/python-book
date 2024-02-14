import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """배의 초기 위치를 설정합니다."""
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 배 이미지를 로드하고 해당 이미지의 rect 속성을 설정합니다.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 각 배를 화면 아래쪽 중앙에 배치합니다.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 배의 중심을 나타내는 소수 값으로 저장합니다.
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 배의 이동을 나타내는 플래그입니다.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """배를 화면 중앙에 배치합니다."""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - 20

    def update(self):
        """이동 플래그에 따라 배의 위치를 업데이트합니다."""
        # 좌우 이동
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        # 위아래 이동
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # rect 객체를 self.center에서 업데이트합니다.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery  # 세로 방향 위치 업데이트

    def blitme(self):
        """현재 위치에 배를 그립니다."""
        self.screen.blit(self.image, self.rect)
