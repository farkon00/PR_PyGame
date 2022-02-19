from __future__ import annotations
import pygame


class Target(pygame.sprite.Sprite):
    """Класс для управления пулями"""

    def __init__(self, game : "Game") -> None:
        super().__init__()

        self.screen : pygame.Surface = game.screen
        self.screen_rect = self.screen.get_rect()
        self.config = game.config

        # Поля для наследовоного класса
        self.color = self.config.target_color
        self.rect = pygame.Rect(0, 0, self.config.target_width, self.config.target_width)
        self.rect.right = self.screen_rect.right

        self.y = float(self.rect.y)
        self._move = self.config.target_speed

    def update(self) -> None:
        """Перемещает пулю вверх"""

        self.y += self._move
        
        self.rect.y = int(self.y)
        if self.y + self.rect.height > self.screen_rect.height or self.y < 0:
            self._move = -self._move
            self.update()

    def draw(self) -> None:
        """Вывод пули на экран"""

        pygame.draw.rect(self.screen, self.color, self.rect)