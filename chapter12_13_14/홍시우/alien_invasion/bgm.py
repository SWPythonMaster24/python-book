import pygame

class Bgm:
    """게임 배경음악을 관리하는 클래스"""
    def __init__(self, ai_game):
        self.ai_game        = ai_game
        self.screen         = ai_game.screen
        self.screen_rect    = self.screen.get_rect()
        self.settings       = ai_game.settings

        # 음악을 재생하는지 여부
        self.paused = False

        # mp3 파일을 load
        pygame.mixer.music.load('./alien_invasion/music/bgm.mp3')

        # Music stream 무한 반복
        pygame.mixer.music.play(-1)

    def _volume_up(self):
        """배경음악의 소리를 키움"""
        v = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(v + 0.1)

    def _volume_down(self):
        """배경음악의 소리를 줄임"""
        v = v = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(v - 0.1)

    def _pause(self):
        """배경음악을 일시정지함"""
        pygame.mixer.music.pause()
        self.paused = True
    
    def _unpause(self):
        """배경음악을 다시재생함"""
        pygame.mixer.music.unpause()
        self.paused = False

