import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # 파이게임, 설정, 화면 객체를 초기화합니다.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 플레이 버튼을 만듭니다.
    play_button = Button(ai_settings, screen, "Play")
    
    # 게임 통계와 스코어보드를 저장할 인스턴스를 생성합니다.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # 배경색을 설정합니다.
    bg_color = (230, 230, 230)
    
    # 배, 총알 그룹, 외계인, 아이템 그룹을 만듭니다.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    item = Group()

    # 외계인 함대를 만듭니다.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 게임의 메인 루프를 시작합니다.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets, item)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, item)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, item)
            gf.update_item(ai_settings, screen, stats, sb, ship, aliens, bullets, item)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, item, play_button)

run_game()
