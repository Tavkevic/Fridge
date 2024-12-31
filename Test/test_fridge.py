import pytest
from Items.shelf import Shelf
from Items.fridge_s import Fridge


@pytest.fixture
def shelf():
    """Создание экземпляра полки для тестирования."""
    return Shelf("TestShelf", 10)  # Создаем экземпляр Shelf с названием "TestShelf" и размером 10


@pytest.fixture
def fridge():
    fridge = Fridge()
    return Fridge()


def test_remove_from_1(fridge):
    shelf1 = Shelf("TestShelf1", 5, [{"name": "Apple", "many": 5}])
    shelf2 = Shelf("TestShelf2", 5, [{"name": "Apple", "many": 5}])

    fridge.app_shelf(shelf1)
    fridge.app_shelf(shelf2)
    fridge.takes({"name": "Apple", "many": 5})

    assert shelf1.inside == []
    assert shelf2.inside == [{"name": "Apple", "many": 5}]


def test_remove_from_2(fridge):
    shelf1 = Shelf("TestShelf1", 5, [{"name": "Apple", "many": 5}])
    shelf2 = Shelf("TestShelf2", 5, [{"name": "Apple", "many": 5}])

    fridge.app_shelf(shelf1)
    fridge.app_shelf(shelf2)
    fridge.takes({"name": "Apple", "many": 7})

    assert shelf1.inside == []
    assert shelf2.inside == [{"name": "Apple", "many": 3}]
