import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """배에서 발사된 총알을 관리하는 클래스"""

    def __init__(self, ai_settings, screen, ship):
        """배의 현재 위치에 총알 객체를 생성합니다."""
        super(Bullet, self).__init__()
        self.screen = screen

        # (0, 0)에 총알 직선을 생성한 다음 올바른 위치를 설정합니다.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 글머리 기호 위치에 십진수 값을 저장합니다.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """글머리 기호를 화면 위로 이동합니다."""
        # 글머리 기호의 소수점 위치를 업데이트합니다.
        self.y -= self.speed_factor
        # 직사각형 위치를 업데이트합니다.
        self.rect.y = self.y

    def draw_bullet(self):
        """화면에 총알을 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)
