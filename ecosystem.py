"""
Модуль, описывающий экосистему и управление симуляцией.
"""

from typing import List, Optional
from organism import Organism, Herbivore, Predator


class Ecosystem:
    """Класс экосистемы, содержащий все организмы и управляющий их взаимодействием."""

    def __init__(self):
        self.organisms: List[Organism] = []

    def add_organism(self, organism: Organism) -> None:
        """Добавляет организм в экосистему."""
        self.organisms.append(organism)

    def find_herbivore(self) -> Optional[Herbivore]:
        """Находит первого живого травоядного в списке."""
        for org in self.organisms:
            if isinstance(org, Herbivore) and org.is_alive():
                return org
        return None

    def step(self) -> None:
        """Выполняет один шаг симуляции: все организмы совершают действия."""
        # Создаём копию списка, чтобы можно было добавлять новых организмов
        for organism in self.organisms[:]:
            if organism.is_alive():
                organism.act(self)
            else:
                # Удаляем мёртвых (можно оставить для статистики)
                print(f"{organism.name} умер")

        # Удаляем мёртвых (проход по списку с конца)
        self.organisms = [org for org in self.organisms if org.is_alive()]

    def get_stats(self) -> str:
        """Возвращает строку со статистикой популяции."""
        herbivores = sum(1 for o in self.organisms if isinstance(o, Herbivore))
        predators = sum(1 for o in self.organisms if isinstance(o, Predator))
        total = len(self.organisms)
        return f"Популяция: всего {total}, травоядных {herbivores}, хищников {predators}"