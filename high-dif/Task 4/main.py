import pygame
import time

from config import Config
from button import Button
from ship import Ship
from bullet import Bullet
from stats import Stats
from target import Target

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.config = Config()
        self.screen : pygame.Surface = pygame.display.set_mode((self.config.width, self.config.height))
        self.stats = Stats(self)
        self.ship = Ship(self)
        self.target = Target(self)

        self.bullets = pygame.sprite.Group()

        self.button = Button(self, "Play")
        self.difs = [Button(self, "Сложность 1", pos=(150, 130)), Button(self, "Сложность 2", pos=(400, 130)), Button(self, "Сложность 3", pos=(650, 130))]

        self.hps = [Ship(self, pos=(i, 0)) for i in range(0, self.config.ship_count * 70 + 1, 70)]
        
        pygame.display.set_caption("Alien Invasion")

    def _update_hp(self):
        self.hps = self.hps[:self.stats.ships_left]

        for i in self.hps:
            i.blit()

    def _fire_bullet(self) -> None:
        """Выстрелевание пулей"""
        if len(self.bullets) < self.config.allowed_bullets and self.stats.game_active:
            bullet = Bullet(self)
            self.bullets.add(bullet)
    
    def _key_down_handler(self, e : pygame.event.Event) -> None:
        """Оброботчик ивентов KEYDOWN"""
        if e.key == pygame.K_w or e.key == pygame.K_UP: # Движение корабля в лево
            self.ship.move = -self.config.ship_speed

        if e.key == pygame.K_s or e.key == pygame.K_DOWN: # Движение корабля в право
            self.ship.move = self.config.ship_speed

        # Движение корабля в право
        if e.key == pygame.K_SPACE: 
                self._fire_bullet()

        if e.key == pygame.K_ESCAPE: # Закрытие игры
            quit()

    def _mouse_handler(self, e : pygame.event.Event) -> None:
        """Оброботчик ивентов мыши"""
        if e.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            if self.button.rect.collidepoint(*mouse_pos) and not self.stats.game_active:
                self.stats.game_active = True

                pygame.mouse.set_visible(False)

                self.config.ship_speed *= self.stats.dif + 1
                self.config.bullet_speed *= self.stats.dif + 1
                self.config.target_speed *= self.stats.dif + 1

                return None

            for j, i in enumerate(self.difs):
                if i.rect.collidepoint(*mouse_pos) and not self.stats.game_active:
                    self.stats.dif = j

                    return None

            self._fire_bullet()

    def _event_handler(self) -> None:
        """Оброботчик ивентов"""
        for e in pygame.event.get():
            if e.type == pygame.QUIT: # Закрытие игры
                exit()

            elif e.type == pygame.KEYDOWN:
                self._key_down_handler(e)

            elif e.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_handler(e)

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_s or e.key == pygame.K_UP or e.key == pygame.K_w or e.key == pygame.K_DOWN: # Остановка корабля
                    self.ship.move = 0

        collisions = pygame.sprite.spritecollide(
            self.target, self.bullets, True
        )

        for i in collisions:
            self.config.increase_speed()

    def _bullets_updating(self) -> None:
        """Работа с пулями"""
        self.bullets.update()

        for i in self.bullets.sprites():
            i.draw()
        for i in self.bullets.copy():
            if i.rect.x >= self.screen.get_rect().width:
                self._ship_hit()
                self.bullets.remove(i)

    def _update_frame(self) -> None:
        """Работа с экраном и объектами"""
        # Работа с кораблём
        self.screen.fill(self.config.bg)
        if self.stats.game_active:
            self.ship.blit()
            
        if self.stats.game_active:
            # Работа с пулями
            self._bullets_updating()

            # Работа с hp
            self._update_hp()

            # Работа с мешенью 
            self.target.update()
            self.target.draw()

        # GUI
        if not self.stats.game_active:
            self.button.draw_button()
            for i in self.difs:
                i.draw_button()

        pygame.display.flip()

    def _ship_hit(self) -> None:
        self.stats.ships_left -= 1

        if self.stats.ships_left < 0:
            self.stats.game_active = False
            self.stats.reset_stats()
            self.config.reset()
            self.hps = [Ship(self, pos=(i, 0)) for i in range(0, self.config.ship_count * 70 + 1, 70)]

        self.bullets.empty()

        # Установка корабля в изначальную позицию
        self.ship.rect.y = self.screen.get_rect().height // 2 - self.ship.rect.height // 2
        self.ship.y = self.ship.rect.y

        pygame.mouse.set_visible(True)

        self._update_frame()

        time.sleep(2)

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""
        
        while True:
            # Оброботчик ивентов
            self._event_handler()

            # Работа с экраном
            self._update_frame()
            

if __name__ == "__main__":
    Game().start_game()