class Settings:
    """외계인 침공의 설정을 저장하는 클래스"""

    def __init__(self):
        """게임 설정 초기화"""
        # 화면 설정
        self.screen_width   = 1200
        self.screen_height  = 800
        self.bg_color       = (230, 230, 230)

        # 우주선 설정
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 탄환 설정
        self.bullet_speed   = 2.5
        self.bullet_width   = 3
        self.bullet_height  = 15
        self.bullet_color   = (60, 60, 60)
        self.bullet_allowed = 3

        # 외계인 설정
        self.alien_speed        =  1.0
        self.fleet_drop_speed   = 10
        self.fleet_direction    = 1     # 1은 오른쪽, -1은 왼쪽

        # 게임을 빠르게 만드는 속도
        self.speedup_scale = 1.1
        # 외계인 점수가 늘어나는 속도
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """게임을 진행하는 동안 변하는 설정 초기화"""
        self.ship_speed     = 1.5
        self.bullet_speed   = 2.5
        self.alien_speed    = 1.0

        self.fleet_direction    = 1
        self.alien_points       = 50

    def increase_speed(self):
        """속도 설정을 높입니다"""
        self.ship_speed     *= self.speedup_scale
        self.bullet_speed   *= self.speedup_scale
        self.alien_speed    *= self.speedup_scale

        self.alien_points   = int(self.alien_points * self.score_scale)
        print(self.alien_points)