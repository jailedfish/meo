"""
Точка входа в симулятор.
"""

from ecosystem import Ecosystem
from organism import Herbivore, Predator


def main():
    """Главная функция, запускающая симуляцию."""
    eco = Ecosystem()

    # Создаём начальные организмы
    rabbit1 = Herbivore("Заяц-1", health=50, energy=40)
    rabbit2 = Herbivore("Заяц-2", health=45, energy=35)
    fox = Predator("Лиса", health=60, energy=50)

    eco.add_organism(rabbit1)
    eco.add_organism(rabbit2)
    eco.add_organism(fox)

    # Запускаем симуляцию на 10 шагов
    for day in range(1, 11):
        print(f"\n--- День {day} ---")
        eco.step()
        print(eco.get_stats())

    print("\nСимуляция завершена.")


if __name__ == "__main__":
    main()
    