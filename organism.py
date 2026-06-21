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

class Herbivore(Organism):
    """Травоядное животное – питается растениями (моделируем через пополнение энергии)."""

    def __init__(self, name: str, health: int, energy: int, plant_food_value: int = 10):
        super().__init__(name, health, energy)
        self.plant_food_value = plant_food_value

    def eat_plant(self) -> None:
        """Поедание растения – восстанавливает энергию."""
        self.energy += self.plant_food_value
        # Небольшое случайное увеличение здоровья от еды
        self.health = min(self.health + 2, 100)

    def reproduce(self) -> 'Herbivore':
        """Размножение – создание нового травоядного с половиной здоровья и энергии."""
        child_health = self.health // 2
        child_energy = self.energy // 2
        self.health -= child_health
        self.energy -= child_energy
        return Herbivore(f"{self.name}_child", child_health, child_energy)

    def act(self, ecosystem: 'Ecosystem') -> None:
        """Действие травоядного за шаг: поиск еды, размножение или движение."""
        if not self.is_alive():
            return

        # Старение
        self.aging()
        if not self.is_alive():
            return

        # Если энергии мало – ищем еду (симулируем поедание растений)
        if self.energy < 30:
            self.eat_plant()  # Упрощённо: всегда находит еду
        # Если энергии и здоровья достаточно – размножаемся
        elif self.energy > 60 and self.health > 50:
            child = self.reproduce()
            ecosystem.add_organism(child)
            print(f"{self.name} размножился, появился {child.name}")
        else:
            # Иначе тратим энергию на движение
            self.energy -= 5
            
