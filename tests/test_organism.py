# tests/test_organism.py
import pytest
from organism import *


def test_herbivore_eat():
    h = Herbivore("Test", health=50, energy=30)
    assert h.energy == 30
    h.eat_plant()
    assert h.energy == 40   # plant_food_value=10
    assert h.health > 50    # должно подрасти

def test_herbivore_reproduce():
    h = Herbivore("Test", health=80, energy=70)
    child = h.reproduce()
    assert child.health == 40
    assert child.energy == 35
    assert h.health == 40   # осталось 40
    assert h.energy == 35