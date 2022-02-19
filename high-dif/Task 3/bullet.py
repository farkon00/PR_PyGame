from __future__ import annotations
import pygame


class Bullet(pygame.sprite.Sprite):
    """Класс для управления пулями"""

    def __init__(self, game : "Game") -> None:
        super().__init__()

        self.screen : pygame.Surface = game.screen
        self.config = game.config

        # Поля для наследовоного класса
        self.color = self.config.bullet_color
        self.rect = pygame.Rect(0, 0, self.config.bullet_width, self.config.bullet_height)
        self.rect.center = game.ship.rect.center

        self.x = float(self.rect.x)

    def update(self) -> None:
        """Перемещает пулю вверх"""

        self.x += self.config.bullet_speed
        
        self.rect.x = int(self.x)

    def draw(self) -> None:
        """Вывод пули на экран"""

        pygame.draw.rect(self.screen, self.color, self.rect)