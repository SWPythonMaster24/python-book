import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """버튼 어트리뷰트를 초기화합니다."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 버튼의 크기와 속성을 설정합니다.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # 버튼의 rect 객체를 만들고 중앙에 배치합니다.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 버튼 메시지는 한 번만 준비하면 됩니다.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """msg를 렌더링된 이미지로 바꾸고 버튼의 텍스트를 가운데에 배치합니다."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # 빈 버튼을 그린 다음 메시지를 그립니다.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
