import pygame

class Hero:
    def __init__(self, game) -> None:
        self.screen : pygame.Surface = game.screen
        self.sreen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("hero.png") # Да-да очень нужен bmp, но оно работает
        self.rect : pygame.Rect = self.image.get_rect()

        self.rect.center = self.sreen_rect.center

    def blit(self) -> None:
        self.screen.blit(self.image, self.rect)

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.screen : pygame.Surface = pygame.display.set_mode((800, 600))
        self.hero : Hero = Hero(self)
        
        pygame.display.set_caption("Task 2")

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""

        while True:
            self.screen.fill((36, 54, 68))

            for e in pygame.event.get():
                if e.type == pygame.QUIT: # Закрытие игры
                    exit()

            self.hero.blit()

            pygame.display.flip()
            

if __name__ == "__main__":
    Game().start_game()