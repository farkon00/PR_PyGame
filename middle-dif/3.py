import pygame

class Rain:
    def __init__(self, game, x, y) -> None:
        self.screen : pygame.Surface = game.screen
        self.screen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("middle-dif\images/rain.jpg")
        self.rect : pygame.Rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.y = y

    def blit(self) -> None:
        self.y += 0.1
        self.rect.y = self.y

        if self.y > self.screen_rect.height:
            return True

        self.screen.blit(self.image, self.rect)

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.screen : pygame.Surface = pygame.display.set_mode((800, 600))
        self.rains = []

        for i in range(int(self.screen.get_rect().width / 80)):
            for j in range(int(self.screen.get_rect().height / 80)):
                self.rains.append(Rain(self, i*90, j*90))
        
        pygame.display.set_caption("Task 3")

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""

        while True:
            self.screen.fill((255, 255, 255))

            for e in pygame.event.get():
                if e.type == pygame.QUIT: # Закрытие игры
                    exit()

            for i in self.rains:
                if i.blit():
                    self.rains.remove(i)

            pygame.display.flip()
            

if __name__ == "__main__":
    Game().start_game()