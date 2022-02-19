import pygame

class Text:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.config = game.config
        self.stats = game.stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 35)

        self.update()

    def _set_dif(self, dif):
        text =f"Сложность : {int(dif+1)}"
        
        self.text_image = self.font.render(text, True, self.text_color) 

        self.text_rect = self.text_image.get_rect()
        self.text_rect.topright = self.screen_rect.topright

        self.screen.blit(self.text_image, self.text_rect)

    def update(self):
        self._set_dif(self.stats.dif)