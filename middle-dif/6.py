import pygame
import random

class Ball:
    def __init__(self, game) -> None:
        self.screen : pygame.Surface = game.screen
        self.screen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("middle-dif\images/ball.jpg")
        self.rect : pygame.Rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = 0
        self.y = 0

    def blit(self) -> None:
        self.y += 0.1
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect)

class Hero:
    def __init__(self, game) -> None:
        self.screen : pygame.Surface = game.screen
        self.sreen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("middle-dif\images/hero.png")
        self.rect : pygame.Rect = self.image.get_rect()
        self.__move : tuple[int, int] = (0, 0)

        self.rect.midbottom = self.sreen_rect.midbottom

    def move(self, x=None, y=None):
        self.__move = (x if x != None else self.__move[0], y if y != None else self.__move[1])

    def blit(self) -> None:
        self.rect.x += self.__move[0]
        self.rect.y += self.__move[1]
        if self.rect.x < 0 or self.rect.x + self.rect.width > 800:
            self.rect.x -= self.__move[0]
        if self.rect.y < 0 or self.rect.y + self.rect.height > 600:
            self.rect.y -= self.__move[1]
        self.screen.blit(self.image, self.rect)

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.screen : pygame.Surface = pygame.display.set_mode((800, 600))
        self.ball = Ball(self)
        self.hero = Hero(self)

        self.missed = 0
        
        pygame.display.set_caption("Task 5")

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""

        while True:
            self.screen.fill((255, 255, 255))

            for e in pygame.event.get():
                if e.type == pygame.QUIT: # Закрытие игры
                    exit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.hero.move(-1)
                    if e.key == pygame.K_RIGHT:
                        self.hero.move(1)

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.hero.move(0)
                    if e.key == pygame.K_RIGHT:
                        self.hero.move(0)

            self.ball.blit()
            self.hero.blit()

            if pygame.sprite.spritecollide(self.ball, [self.hero], False):
                self.ball = Ball(self)

            if self.ball.rect.y >= self.screen.get_rect().height: 
                self.ball = Ball(self)
                self.missed += 1

            if self.missed >= 3:
                exit()

            pygame.display.flip()
            

if __name__ == "__main__":
    Game().start_game()