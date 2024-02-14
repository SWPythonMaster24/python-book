import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """점수 정보를 보고하는 클래스"""

    def __init__(self, ai_settings, screen, stats):
        """채점 속성을 초기화합니다."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 채점 정보에 대한 글꼴 설정.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 초기 점수 이미지를 준비합니다.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """점수를 렌더링된 이미지로 변환합니다."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        # 화면 오른쪽 상단에 점수를 표시합니다.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """최고 점수를 렌더링된 이미지로 변환합니다."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color)

        # 최고 점수를 화면 상단에 중앙에 배치합니다.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """레벨을 렌더링된 이미지로 전환합니다."""
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)
        
        # 레벨을 점수 아래에 배치합니다.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """남은 선박 수를 표시합니다."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        """화면에 점수를 표시합니다."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 배를 그립니다.
        self.ships.draw(self.screen)
