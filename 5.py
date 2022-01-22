import pygame


class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.config : Config = Config()
        self.screen : pygame.Surface = pygame.display.set_mode((self.config.width, self.config.height))
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        
        pygame.display.set_caption("Alien Invasion")

    def __fire_bullet(self) -> None:
        """Выстрелевание пулей"""
        if len(self.bullets) < self.config.allowed_bullets:
            bullet = Bullet(self)
            self.bullets.add(bullet)
    
    def __key_down_handler(self, e : pygame.event.Event) -> None:
        """Оброботчик ивентов KEYDOWN"""
        if e.key == pygame.K_w or e.key == pygame.K_UP: # Движение корабля в лево
            self.ship.move = -self.config.ship_speed

        if e.key == pygame.K_s or e.key == pygame.K_DOWN: # Движение корабля в право
            self.ship.move = self.config.ship_speed

        # Движение корабля в право
        if e.key == pygame.K_SPACE: 
                self.__fire_bullet()

        if e.key == pygame.K_ESCAPE: # Закрытие игры
            quit()

    def __mouse_handler(self, e : pygame.event.Event) -> None:
        """Оброботчик ивентов мыши"""
        if e.button == 1:
            self.__fire_bullet()

    def __event_handler(self) -> None:
        """Оброботчик ивентов"""
        for e in pygame.event.get():
            if e.type == pygame.QUIT: # Закрытие игры
                exit()

            elif e.type == pygame.KEYDOWN:
                self.__key_down_handler(e)

            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.__mouse_handler(e)

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_w or e.key == pygame.K_UP or e.key == pygame.K_s or e.key == pygame.K_DOWN: # Остановка корабля
                    self.ship.move = 0

    def __bullets_updating(self) -> None:
        """Работа с пулями"""
        self.bullets.update()

        for i in self.bullets.sprites():
            i.draw()
        for i in self.bullets.copy():
            if i.rect.x >= 800:
                self.bullets.remove(i)

    def __update_frame(self) -> None:
        """Работа с экраном и объектами"""
        # Работа с кораблём
        self.screen.fill(self.config.bg)
        self.ship.blit()

        self.__bullets_updating()

        pygame.display.flip()

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""
        
        while True:
            # Оброботчик ивентов
            self.__event_handler()

            # Работа с экраном
            self.__update_frame()


class Bullet(pygame.sprite.Sprite):
    """Класс для управления пулями"""

    def __init__(self, game) -> None:
        super().__init__()

        self.screen : pygame.Surface = game.screen
        self.config = game.config

        # Поля для наследовоного класса
        self.color = self.config.bullet_color
        self.rect = pygame.Rect(0, 0, self.config.bullet_width, self.config.bullet_height)
        self.rect.left = self.screen.get_rect().left
        self.rect.y = game.ship.rect.y + game.ship.rect.height // 2

        self.x = float(self.rect.x)

    def update(self) -> None:
        """Перемещает пулю вверх"""

        self.x += self.config.bullet_speed
        
        self.rect.x = int(self.x)

    def draw(self) -> None:
        """Вывод пули на экран"""

        pygame.draw.rect(self.screen, self.color, self.rect)
            

class Ship:
    """Класс для управления кораблём"""
    def __init__(self, game) -> None:
        self.screen : pygame.Surface = game.screen
        self.sreen_rect : pygame.Rect = game.screen.get_rect()

        self.image : pygame.image = pygame.image.load("ship.png")
        self.rect : pygame.Rect = self.image.get_rect()
        self.move : float = 0

        self.rect.left = self.sreen_rect.left
        self.rect.y = self.sreen_rect.height // 2 - self.rect.height // 2

        self.y : float = float(self.rect.y)

    def blit(self) -> None:
        """Рисует корабль"""
        if  self.y + self.move > 0 and self.y + self.move + self.rect.height < self.sreen_rect.height:
            self.y += self.move
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect)


class Config:
    """Класс для конфига игры"""
    def __init__(self) -> None:
        self.width : int = 800
        self.height : int = 600
        self.bg : tuple[int] = (230, 230, 230)

        self.ship_speed : float = 1.5

        self.bullet_speed : float = 1
        self.bullet_width : int = 15
        self.bullet_height : int = 3
        self.bullet_color : tuple[int] = (60, 60, 60)
        self.allowed_bullets = 3


if __name__ == "__main__":
    Game().start_game()