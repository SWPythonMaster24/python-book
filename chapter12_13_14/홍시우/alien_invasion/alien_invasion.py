import sys
from time import sleep

import pygame

from settings import Settings
from bgm import Bgm
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""

    def __init__(self):
        """게임을 초기화 하고 게임 자원을 만듭니다."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Bgm을 재생하는 인스턴스를 만듭니다
        self.bgm = Bgm(self)

        # 게임 기록을 저장하고 점수판을 표시할 인스턴스를 만듭니다
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # 비활성 상태로 게임을 시작합니다
        self.game_active = False

        # [플레이] 버튼을 만듭니다
        self.play_button = Button(self, "Play")

    def run_game(self):
        """게임의 메인 루프를 시작합니다"""
        while True:
                self.check_events()

                if self.game_active:
                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()

                self.update_screen()
                self.clock.tick(60)                
    
    def check_events(self):
        """키 입력과 마우스 이벤트에 응답합니다"""
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            self._check_play_button(mouse_pos)
                        elif event.type == pygame.KEYDOWN:
                            self._check_keydown_events(event)
                        elif event.type == pygame.KEYUP:
                            self._check_keyup_events(event)
                            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
        elif event.key == pygame.K_UP:
            self.bgm._volume_up()
        elif event.key == pygame.K_DOWN:
            self.bgm._volume_down()
        elif event.key == pygame.K_PAUSE:
            if self.bgm.paused:
                self.bgm._unpause()
            else:
                self.bgm._pause()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False        
                            
    def _fire_bullet(self):
        """새 탄환을 만들어 탄환 그룹에 추가합니다"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """탄환 위치를 업데이트하고 사라진 탄환을 제거합니다"""
        self.bullets.update()
        # 사라진 탄환을 제거합니다.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """탄환과 외계인의 충돌을 관리합니다"""
        # 충돌한 탄환과 외계인을 제거합니다.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # 남아 있는 탄환을 제거하고 함대를 새로 만듭니다
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    
    def update_screen(self):
        """화면의 이미지를 업데이트하고 화면을 새로 그립니다"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # 점수 정보를 그립니다
        self.sb.show_score()

        # 게임이 비활성 상태면 [플레이] 버튼을 그립니다
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """외계인 함대를 만듭니다"""
        # 외계인을 하나를 만들고, 공간이 없을 때 까지 계속 추가합니다
        # 외계인 사이의 공간은 외계인 너비와 같습니다
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 한 줄이 끝났으니 x 값은 초기화 하고 y값은 늘립니다
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """외계인 하나를 만들어 배치합니다"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """함대에 속한 외계인의 위치를 모두 업데이트합니다"""
        self._chekc_fleet_edges()
        self.aliens.update()

        # 외계인과 우주선의 충돌 검색
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 화면 하단에 도달한 외계인을 찾습니다
            self._check_alien_bottom()

    def _chekc_fleet_edges(self):
        """외계인이 화면 경계에 도달했을 때 반응합니다"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """함대 전체를 한 줄 내리고 좌우 방향을 바꿉니다"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """외계인이 우주선에 충돌할 때 작업"""
        if self.stats.ships_left > 0:
            # ships_left 값을 줄이고 점수판을 업데이트 합니다
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # 남아 있는 탄환과 외계인을 모두 제거합니다
            self.bullets.empty()
            self.aliens.empty()

            # 함대를 새로 만들고 우주선을 화면 하단 중앙으로 이동시킵니다
            self._create_fleet()
            self.ship.center_ship()

            # 일시중지
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_alien_bottom(self):
        """화면 하단에 도달한 외계인이 있는지 확인합니다"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 우주선에 외계인이 충돌할 때와 똑같이 반응합니다
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """플레이어가 [플레이] 버튼을 클릭하면 게임을 시작합니다"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 게임 설정 초기화
            self.settings.initialize_dynamic_settings()

            # 게임 기록 초기화
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # 남아 있는 탄환과 외계인을 모두 제거합니다
            self.bullets.empty()
            self.aliens.empty()

            # 함대를 새로 만들고 우주선을 화면 하단 중앙으로 이동시킵니다
            self._create_fleet()
            self.ship.center_ship()

            # 마우스 커서를 숨깁니다
            pygame.mouse.set_visible(False)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()