from __future__ import annotations
from config import Config
import pygame


class Alien(pygame.sprite.Sprite):
    """Класс представляющий одного пришельца"""
    def __init__(self, game : "Game", x : float, y : float) -> None:
        """Инициализирует пришельца"""
        super().__init__()

        self.screen : pygame.Surface = game.screen
        self.screen_rect : pygame.Rect = game.screen.get_rect()
        self.config : Config = game.config

        self.image : pygame.image = pygame.image.load("images/alien.bmp")
        self.rect : pygame.Rect = self.image.get_rect()
        self.direction : float = self.config.x_alien_speed
        
        self.x = float(x)
        self.y = float(y)

        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        """Перемещает пришельца"""
        self.x += self.direction

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    @property
    def not_in_bounce(self) -> bool:
        if 0 > self.x + self.direction or self.x + self.direction + self.rect.width > self.screen_rect.width:
            return True