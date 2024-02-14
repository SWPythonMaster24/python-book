import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien
from item import Item

import random



def check_keydown_events(event, ai_settings, screen, ship, bullets, item):
    """키 누름에 응답합니다."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """키 릴리스에 응답합니다."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        ship.moving_down = False
        ship.moving_up = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        ship.moving_down = False
        ship.moving_up = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
        ship.moving_right = False
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        ship.moving_right = False
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets, item):
    """키 누름과 마우스 이벤트에 응답합니다."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, item)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, item, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, item, mouse_x, mouse_y):
    """플레이어가 플레이를 클릭하면 새 게임을 시작합니다."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 게임 설정을 초기화합니다.
        ai_settings.initialize_dynamic_settings()

        # 마우스 커서를 숨깁니다.
        pygame.mouse.set_visible(False)

        # 게임 통계를 재설정합니다.
        stats.reset_stats()
        stats.game_active = True

        # 점수판 이미지를 초기화합니다.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 외계인과 총알 목록을 비웁니다.
        aliens.empty()
        bullets.empty()
        item.empty()

        # 랜덤 아이템을 생성합니다.
        create_item(ai_settings, screen, item)

        # 새 함대를 생성하고 함선을 중앙에 배치합니다.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()



def fire_bullet(ai_settings, screen, ship, bullets):
    """아직 제한에 도달하지 않은 경우 총알을 발사합니다."""
    # 새 총알을 생성하고 총알 그룹에 추가합니다.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, item, play_button):
    """화면의 이미지를 업데이트하고 새 화면으로 넘깁니다."""
    # 루프를 통과할 때마다 화면을 다시 그립니다.
    screen.fill(ai_settings.bg_color)

    # 배와 외계인 뒤에 있는 모든 총알을 다시 그립니다.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    item.draw(screen)

    # 점수 정보를 그립니다.
    sb.show_score()

    # 게임이 비활성 상태이면 플레이 버튼을 그립니다.
    if not stats.game_active:
        play_button.draw_button()

    # 가장 최근에 그린 화면을 표시합니다.
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, item):
    """총알의 위치를 업데이트하고 오래된 총알을 제거합니다."""
    # 총알 위치를 업데이트합니다.
    bullets.update()

    # 사라진 총알을 제거합니다.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets, item)


def check_high_score(stats, sb):
    """새로운 최고 점수가 있는지 확인합니다."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets, item):
    """총알-외계인 충돌에 대응합니다."""
    # 충돌한 총알과 외계인을 모두 제거합니다.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 전체 함대가 파괴되면 새 레벨을 시작합니다.
        bullets.empty()
        ai_settings.reset_item_option()
        ai_settings.increase_speed()

        # 레벨을 높입니다.
        stats.level += 1
        sb.prep_level()

        create_item(ai_settings, screen, item)
        create_fleet(ai_settings, screen, ship, aliens)



def check_fleet_edges(ai_settings, aliens):
    """외계인이 가장자리에 도달하면 적절히 대응합니다."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """전체 함대를 버리고 함대의 방향을 변경합니다."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, item):
    """함선이 외계인에게 피격당하면 대응합니다."""
    if stats.ships_left > 0:
        # ships_left를 감소시킵니다.
        stats.ships_left -= 1

        # 점수판을 업데이트합니다.
        sb.prep_ships()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # 외계인과 총알 목록을 비웁니다.
    aliens.empty()
    bullets.empty()
    item.empty()

    # 새 함대를 생성하고 함선을 중앙에 배치합니다.
    create_fleet(ai_settings, screen, ship, aliens)
    create_item(ai_settings, screen, item)
    ship.center_ship()

    # 아이템 효과를 초기화합니다.
    ai_settings.reset_item_option()

    # 일시정지합니다.
    sleep(0.5)


def item_hit(ai_settings, aliens, item):
    option = random.randint(1, 4)

    ai_settings.item_option = option

    if option == 1:
        ai_settings.bullet_width = 200
    elif option == 2:
        ai_settings.alien_speed_factor += 0.5
    elif option == 3:
        ai_settings.alien_speed_factor -= 0.5
    elif option == 4:
        # 제거할 스프라이트의 개수를 그룹의 크기와 비교하여 조정
        num_to_remove = min(len(aliens), 3)

        # aliens 그룹에서 랜덤하게 스프라이트를 선택
        aliens_to_remove = random.sample(aliens.sprites(), num_to_remove)

        # 선택된 스프라이트를 그룹에서 제거
        for alien in aliens_to_remove:
            aliens.remove(alien)



    # 아이템을 없앱니다
    item.empty()


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, item):
    """외계인이 화면 하단에 도달했는지 확인합니다."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 우주선이 충돌한 경우와 동일하게 처리합니다.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, item)
            break


def update_item(ai_settings, screen, stats, sb, ship, aliens, bullets, item):
    """
    함대가 가장자리에 있는지 확인합니다,
    그런 다음 함대에 있는 모든 외계인의 위치를 업데이트합니다.
    """
    # check_fleet_edges(ai_settings, aliens)
    # aliens.update()

    # 아이템과 우주선의 충돌을 찾습니다.
    if pygame.sprite.spritecollideany(ship, item):
        item_hit(ai_settings, aliens, item)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, item):
    """
    함대가 가장자리에 있는지 확인합니다,
    그런 다음 함대에 있는 모든 외계인의 위치를 업데이트합니다.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 외계인과 우주선의 충돌을 찾습니다.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, item)

    # 화면 하단에 충돌하는 외계인을 찾습니다.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, item)


def get_number_aliens_x(ai_settings, alien_width):
    """한 줄에 맞는 외계인 수를 결정합니다."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """화면에 맞는 에일리언의 행 수를 결정합니다."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """외계인을 생성하여 행에 배치합니다."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """전체 외계인 함대를 생성합니다."""
    # 외계인을 생성하고 연속된 외계인 수를 구합니다.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # 외계인 함대를 만듭니다.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def create_item(ai_settings, screen, item):
    item.add(Item(ai_settings, screen))
