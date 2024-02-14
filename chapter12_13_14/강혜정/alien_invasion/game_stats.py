from pathlib import Path 
import json

class GameStats:
    """외계인 침공 게임 기록"""

    def __init__(self, ai_game):
        """기록 초기화"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 최고 점수는 초기화하지 않습니다
        self._get_high_score()

    def _get_high_score(self):
        """최고 점수를 가지고 옵니다"""
        try:
            path = Path('high_score.json')
            if path.exists():
                contents = path.read_text()
                high_score = json.loads(contents)
                self.high_score = high_score
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """게임을 진행하는 동안 변하는 기록 초기화"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1