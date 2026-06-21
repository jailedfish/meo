"""
Вспомогательные функции для симуляции.
"""

import random

def random_health(min_val: int = 20, max_val: int = 80) -> int:
    """Генерирует случайное значение здоровья."""
    return random.randint(min_val, max_val)

def clamp(value: int, low: int, high: int) -> int:
    """Ограничивает значение заданным диапазоном."""
    return max(low, min(value, high))
