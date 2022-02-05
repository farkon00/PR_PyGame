import pygame

class Star:
    def __init__(self, game, x, y) -> None:
        self.screen : pygame.Surface = game.screen
        self.sreen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("middle-dif\images\star.png")
        self.rect : pygame.Rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def blit(self) -> None:
        self.screen.blit(self.image, self.rect)

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.screen : pygame.Surface = pygame.display.set_mode((800, 600))
        self.stars = []

        for i in range(int(self.screen.get_rect().width / 90)):
            for j in range(int(self.screen.get_rect().height / 90)):
                self.stars.append(Star(self, i*90, j*90))
        
        pygame.display.set_caption("Task 1")

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""

        while True:
            self.screen.fill((255, 255, 255))

            for e in pygame.event.get():
                if e.type == pygame.QUIT: # Закрытие игры
                    exit()

            for i in self.stars:
                i.blit()

            pygame.display.flip()
            

if __name__ == "__main__":
    Game().start_game()