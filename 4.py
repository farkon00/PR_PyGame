import pygame

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.screen : pygame.Surface = pygame.display.set_mode((800, 600))
        
        pygame.display.set_caption("Task 4")

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""

        while True:
            self.screen.fill((255, 255, 255))

            for e in pygame.event.get():
                if e.type == pygame.QUIT: # Закрытие игры
                    exit()
                if e.type == pygame.KEYDOWN: 
                    print(e.key)

            pygame.display.flip()
            

if __name__ == "__main__":
    Game().start_game()