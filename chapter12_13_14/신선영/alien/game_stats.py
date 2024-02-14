class GameStats():
    """외계인 침공에 대한 통계를 추적합니다."""
    
    def __init__(self, ai_settings):
        """통계를 초기화합니다."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 비활성 상태에서 게임을 시작합니다.
        self.game_active = False
        
        # 최고 점수는 절대 초기화되지 않습니다.
        self.high_score = 0
        
    def reset_stats(self):
        """게임 중 변경될 수 있는 통계를 초기화합니다."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
