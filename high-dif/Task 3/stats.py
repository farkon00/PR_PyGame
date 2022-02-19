from __future__ import annotations

class Stats:
    """Статистика по игре"""
    def __init__(self, game : "Game") -> None:
        self.config = game.config
        self.high_score = 0

        self.reset_stats()

    def reset_stats(self) -> None:
        self.ships_left = self.config.ship_count
        self.game_active = False
        self.score = 0
        self.wave = 1