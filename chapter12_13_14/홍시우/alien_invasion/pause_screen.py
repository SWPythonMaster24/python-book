import pygame.font

from bgm import Bgm

class PauseScreen:
    """일시 정지 화면을 관리하는 클래스"""
    def __init__(self, ai_game):
        self.ai_game        = ai_game
        self.screen         = ai_game.screen
        self.screen_rect    = self.screen.get_rect()
        self.settings       = ai_game.settings
        self.bgm            = ai_game.bgm

    