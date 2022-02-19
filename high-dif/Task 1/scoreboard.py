import pygame


import pygame

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.config = game.config
        self.stats = game.stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 35)

        self.update()

    def _update_score(self):
        text_score =f"Счёт : {int(self.stats.score)}"
        
        self.text_image_score = self.font.render(text_score, True, self.text_color) 

        self.text_rect_score = self.text_image_score.get_rect()
        self.text_rect_score.topright = self.screen_rect.topright

        self.screen.blit(self.text_image_score, self.text_rect_score)

    def _update_high(self):
        text_high =f"Рекорд : {int(self.stats.high_score)}"

        self.text_image_high = self.font.render(text_high, True, self.text_color) 

        self.text_rect_high = self.text_image_high.get_rect()
        self.text_rect_high.topright = self.screen_rect.topright
        self.text_rect_high.y += self.text_rect_score.height

        self.screen.blit(self.text_image_high, self.text_rect_high)

    def _update_wave(self):
        if self.stats.game_active:
            text_wave =f"Волна : {int(self.stats.wave)}"

            self.text_image_wave = self.font.render(text_wave, True, self.text_color) 

            self.text_rect_wave = self.text_image_wave.get_rect()
            self.text_rect_wave.topright = self.text_rect_high.topright
            self.text_rect_wave.y += self.text_rect_high.height

            self.screen.blit(self.text_image_wave, self.text_rect_wave)

    def update(self):
        self._update_score()
        self._update_high()
        self._update_wave()

    def check_high_score(self):
        """Проверяет, появился ли новый рекорд"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score