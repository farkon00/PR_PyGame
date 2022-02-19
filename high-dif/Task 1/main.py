import pygame
import time

from config import Config
from button import Button
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from stats import Stats

class Game:
    """Класс для управления ресурсами, поведением и запуском игры"""

    def __init__(self) -> None:
        """Иницаилизирует игру и ресурсы"""

        pygame.init()

        self.config = Config()
        self.screen : pygame.Surface = pygame.display.set_mode((self.config.width, self.config.height))
        self.stats = Stats(self)
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_flit()

        self.button = Button(self, "Play")
        self.scoreboard = Scoreboard(self)
        self.hps = [Ship(self, pos=(i, 0)) for i in range(0, self.config.ship_count * 70 + 1, 70)]
        
        pygame.display.set_caption("Alien Invasion")

    def _create_flit(self) -> None:
        """Создание флота пришельцов"""

        alien = Alien(self, 0, 0)

        # Максимальные координаты на которых может появится пришелец
        max_x = self.screen.get_rect().width - (alien.rect.width * 2)
        max_y = self.screen.get_rect().height - self.ship.rect.height * 5

        for x in range(alien.rect.width, max_x, alien.rect.width * 2): # Итерирует через все столбцы
            for y in range(alien.rect.height, max_y, alien.rect.height * 2): # Итерирует через все строки
                self.aliens.add(Alien(self, x, y))

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
        if e.key == pygame.K_a or e.key == pygame.K_LEFT: # Движение корабля в лево
            self.ship.move = -self.config.ship_speed

        if e.key == pygame.K_d or e.key == pygame.K_RIGHT: # Движение корабля в право
            self.ship.move = self.config.ship_speed

        # Движение корабля в право
        if e.key == pygame.K_SPACE: 
            self._fire_bullet()
        if e.key == pygame.K_p:
            self.stats.game_active = True

            pygame.mouse.set_visible(False)

        if e.key == pygame.K_ESCAPE: # Закрытие игры
            quit()

    def _mouse_handler(self, e : pygame.event.Event) -> None:
        """Оброботчик ивентов мыши"""
        if e.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            if self.button.rect.collidepoint(*mouse_pos) and not self.stats.game_active:
                self.stats.game_active = True

                pygame.mouse.set_visible(False)

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
                if e.key == pygame.K_a or e.key == pygame.K_LEFT or e.key == pygame.K_d or e.key == pygame.K_RIGHT: # Остановка корабля
                    self.ship.move = 0

    def _bullets_updating(self) -> None:
        """Работа с пулями"""
        self.bullets.update()

        for i in self.bullets.sprites():
            i.draw()
        for i in self.bullets.copy():
            if i.rect.y <= 0:
                self.bullets.remove(i)

        # Создание новой волны
        if not self.aliens:
            self.config.increase_speed()

            self.stats.score += 100 * self.stats.wave
            self.stats.wave += 1

            self._create_flit()

    def _aliens_updating(self) -> None:
        aliens = self.aliens.sprites()

        is_direction_changed = False
        for i in aliens:
            if i.not_in_bounce and not is_direction_changed:
                for j in aliens:
                    j.direction = -j.direction
                    j.y += self.config.y_alien_speed
                is_direction_changed = True

        self.aliens.update()
        self.aliens.draw(self.screen)

    def _update_frame(self) -> None:
        """Работа с экраном и объектами"""
        # Работа с кораблём
        self.screen.fill(self.config.bg)
        if self.stats.game_active:
            self.ship.blit()
            
        if self.stats.game_active:
            # Работа с пулями
            self._bullets_updating()

            # Работа с пришельцами
            self._aliens_updating()

            # Работа с hp
            self._update_hp()

        # GUI
        if not self.stats.game_active:
            self.button.draw_button()
        self.scoreboard.update()

        pygame.display.flip()

    def _ship_hit(self) -> None:
        self.stats.ships_left -= 1

        if self.stats.ships_left < 0:
            self.stats.game_active = False
            self.scoreboard.check_high_score()
            self.stats.reset_stats()
            self.config.reset()
            self.hps = [Ship(self, pos=(i, 0)) for i in range(0, self.config.ship_count * 70 + 1, 70)]

        self.aliens.empty()
        self.bullets.empty()

        self._create_flit()

        # Установка корабля в изначальную позицию
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.ship.x = self.ship.rect.x

        pygame.mouse.set_visible(True)

        self._update_frame()

        time.sleep(2)

    def _check_aliens_botttom(self) -> None:
        for i in self.aliens.sprites():
            if i.rect.y + i.rect.height >= self.config.height:
                self._ship_hit()
                break


    def _check_collisions(self) -> None:
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        self.stats.score += 20 * len(collisions) * self.stats.wave

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        else:
            self._check_aliens_botttom()

    def start_game(self) -> None:
        """Запуск основного цикла игры. Блокирует!"""
        
        while True:
            # Оброботчик ивентов
            self._event_handler()

            # Работа с экраном
            self._update_frame()

            if self.stats.game_active:
                # Работа с колизиями
                self._check_collisions()
            

if __name__ == "__main__":
    Game().start_game()