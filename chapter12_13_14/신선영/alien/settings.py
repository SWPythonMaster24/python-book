class Settings():
    """외계인 침공에 대한 모든 설정을 저장하는 클래스입니다."""

    def __init__(self):
        """게임의 정적 설정을 초기화합니다."""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 함선 설정
        self.ship_limit = 3
            
        # 총알 설정
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 외계인 설정
        self.fleet_drop_speed = 10
            
        # 게임 속도를 가속화하는 비율
        self.speedup_scale = 1.1
        # 외계인 점수를 가속화하는 비율
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

        # 아이템 설정
        self.item_option = 0

    def initialize_dynamic_settings(self):
        """게임 진행 중에 변경되는 설정을 초기화합니다."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # 점수
        self.alien_points = 50
    
        # fleet_direction이 1이면 오른쪽으로, -1이면 왼쪽으로 이동합니다.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """게임 속도 설정과 외계인 점수를 증가시킵니다."""
        self.item_option = 0
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)

    def reset_item_option(self):
        print(self.item_option)
        """아이템 효과를 초기화합니다."""
        if self.item_option != 0:
            if self.item_option == 1:
                self.bullet_width = 3
            elif self.item_option == 2:
                self.alien_speed_factor -= 0.5
            elif self.item_option == 3:
                self.alien_speed_factor += 0.5

        self.item_option = 0