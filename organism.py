"""
Модуль, описывающий организмы в экосистеме.
Содержит базовый класс Organism и его наследников.
"""

import random
from abc import ABC, abstractmethod


class Organism(ABC):
    """Абстрактный базовый класс для всех организмов."""

    def __init__(self, name: str, health: int, energy: int):
        """
        Инициализация организма.

        :param name: Имя или вид организма.
        :param health: Количество здоровья (0 - мёртв).
        :param energy: Уровень энергии, расходуется на действия.
        """
        self.name = name
        self.health = health
        self.energy = energy
        self.age = 0
        self.alive = True

    def is_alive(self) -> bool:
        """Проверяет, жив ли организм."""
        return self.alive and self.health > 0

    def take_damage(self, damage: int) -> None:
        """Наносит урон здоровью."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def aging(self) -> None:
        """Увеличивает возраст и уменьшает здоровье с течением времени."""
        self.age += 1
        # Каждый шаг теряем 1 здоровье от старости
        self.take_damage(1)

    @abstractmethod
    def act(self, ecosystem: 'Ecosystem') -> None:
        """
        Выполняет действие организма за один шаг симуляции.
        :param ecosystem: Ссылка на экосистему для взаимодействия.
        """
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, health={self.health}, energy={self.energy})"