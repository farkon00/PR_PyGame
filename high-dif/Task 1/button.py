from __future__ import annotations

import pygame

class Button:
    def __init__(self, game : "Game", text : str):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.text = text

        self.width, self.height = 200, 200
        self.color = (0, 230, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prepare_msg(self.text)

    def _prepare_msg(self, text : str):
        """Создаёт объект для текста и подготавливает его"""
        self.text_image = self.font.render(text, True, self.text_color, self.color) 

        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text_image, self.text_rect)