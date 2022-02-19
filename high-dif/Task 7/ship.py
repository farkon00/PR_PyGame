from __future__ import annotations
import pygame

class Ship:
    """Класс для управления кораблём"""
    def __init__(self, game : "Game", pos=None) -> None:
        self.screen : pygame.Surface = game.screen
        self.screen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("images/ship.png")
        self.rect : pygame.Rect = self.image.get_rect()
        self.move : float = 0

        if pos:
            self.rect.topleft = pos
        else:
            self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def blit(self) -> None:
        """Рисует корабль"""
        if  self.x + self.move > 0 and self.x + self.move + self.rect.width < self.screen_rect.width:
            self.x += self.move
        self.rect.x = self.x

        self.screen.blit(self.image, self.rect)
