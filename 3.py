import pygame

class Ship:
    def __init__(self, game) -> None:
        self.screen : pygame.Surface = game.screen
        self.sreen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("ship.png") # Да-да очень нужен bmp, но оно работает + ну представим, что это ракета
        self.rect : pygame.Rect = self.image.get_rect()
        self.__move : tuple[int, int] = (0, 0)

        self.rect.center = self.sreen_rect.center

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
        self.ship : Ship = Ship(self)
        
        pygame.display.set_caption("Task 3")

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""

        while True:
            self.screen.fill((36, 54, 68))

            for e in pygame.event.get():
                if e.type == pygame.QUIT: # Закрытие игры
                    exit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.ship.move(-1)
                    if e.key == pygame.K_RIGHT:
                        self.ship.move(1)
                    if e.key == pygame.K_UP:
                        self.ship.move(y=-1)
                    if e.key == pygame.K_DOWN:
                        self.ship.move(y=1)

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.ship.move(0)
                    if e.key == pygame.K_RIGHT:
                        self.ship.move(0)
                    if e.key == pygame.K_UP:
                        self.ship.move(y=0)
                    if e.key == pygame.K_DOWN:
                        self.ship.move(y=0)

            self.ship.blit()

            pygame.display.flip()
            

if __name__ == "__main__":
    Game().start_game()