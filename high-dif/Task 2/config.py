class Config:
    """Класс для конфига игры"""
    def __init__(self) -> None:
        # Настройки экрана
        self.width = 800
        self.height = 600
        self.bg = (230, 230, 230)

        # Настройки корабля
        self.ship_count = 3

        # Настройки пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 3

        # Настройки пришельцев
        self.y_alien_speed = 20

        # Усложнение игры по уровням
        self.speed_scale = 1.1

        self.reset()

    def reset(self):
        self.ship_speed : float = 1.5

        self.bullet_speed : float = 1

        self.x_alien_speed : float = 0.2

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.x_alien_speed *= self.speed_scale
