import pytest
from Items.shelf import Shelf


@pytest.fixture
def shelf():
    """Создание экземпляра полки для тестирования."""
    return Shelf("TestShelf", 10)  # Создаем экземпляр Shelf с названием "TestShelf" и размером 10


def test_put_item(shelf):
    item = {"name": "Apple", "many": 5}
    shelf = shelf
    shelf.put(item)  # Используем метод put для добавления предмета на полку

    # Проверки, чтобы убедиться, что предмет был добавлен правильно
    assert len(shelf.inside) == 1  # Проверяем, что на полке один предмет
    assert shelf.inside[0]["name"] == "Apple"  # Проверяем, что название предмета "Apple"
    assert shelf.inside[0]["many"] == 5  # Проверяем, что количество предметов равно 5
    assert shelf.free_place == 5  # Проверяем, что свободное место на полке равно 5


def test_put_multiple_items_same_name(shelf):
    item1 = {"name": "Apple", "many": 5}
    item2 = {"name": "Apple", "many": 3}

    shelf.put(item1)
    shelf.put(item2)

    # Check if the item count has increased correctly
    assert len(shelf.inside) == 1
    assert shelf.inside[0]["many"] == 8  # 5 + 3
    assert shelf.free_place == 2  # Total size - total items


def test_put_item_not_enough_space(shelf):
    item1 = {"name": "Apple", "many": 10}
    item2 = {"name": "Banana", "many": 3}

    shelf.put(item1)
    shelf.put(item2)

    assert len(shelf.inside) == 1  # still only one item
    assert shelf.inside[0]["many"] == 10
    assert shelf.free_place == 0  # no free space


def test_take_item(shelf):
    item = {"name": "Apple", "many": 5}
    shelf.put(item)

    take_item = {"name": "Apple", "many": 2}
    shelf.take(take_item)  # Assuming spice is empty here

    assert shelf.inside[0]["many"] == 3  # Should reduce the amount
    assert shelf.free_place == 7  # Total size - total items


def test_take_item_not_enough_available(shelf):
    item = {"name": "Apple", "many": 5}
    shelf.put(item)

    take_item = {"name": "Apple", "many": 6}  # More than available
    shelf.take(take_item)

    assert len(shelf.inside) == 1  # Still only one item
    assert shelf.inside[0]["many"] == 5  # No change as it couldn't remove enough
    assert shelf.free_place == 5  # Free space should still be the same


def test_remove_item(shelf):
    item = {"name": "Apple", "many": 5}
    shelf.put(item)
    shelf.take(item)
    assert len(shelf.inside) == 0  # Should be empty
    assert shelf.free_place == 10  # All space is free now