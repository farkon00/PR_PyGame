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
            self.rect.left = self.screen_rect.left
            self.rect.y = self.screen_rect.height // 2 - self.rect.height // 2

            self.y : float = float(self.rect.y)

        self.y = float(self.rect.y)

    def blit(self) -> None:
        """Рисует корабль"""
        if  self.y + self.move > 0 and self.y + self.move + self.rect.height < self.screen_rect.height:
            self.y += self.move
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect)
