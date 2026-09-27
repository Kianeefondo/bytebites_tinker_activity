from models import Category, Customer, Item, Transaction


def test_order_total_is_correct():
    drinks = Category("Drinks")
    soda = Item("Large Soda", 2.50, drinks, 4.7)
    tea = Item("Iced Tea", 2.00, drinks, 4.5)

    order = Transaction()
    order.add_item(soda)
    order.add_item(tea)

    assert order.calculate_total() == 4.50


def test_empty_order_total_is_zero():
    order = Transaction()

    assert order.calculate_total() == 0.0


def test_filter_menu_items_by_category():
    drinks = Category("Drinks")
    desserts = Category("Desserts")

    soda = Item("Large Soda", 2.50, drinks, 4.7)
    tea = Item("Iced Tea", 2.00, drinks, 4.5)
    cookie = Item("Chocolate Cookie", 3.25, desserts, 4.9)

    drinks.add_item(soda)
    drinks.add_item(tea)
    desserts.add_item(cookie)

    assert [item.get_name() for item in drinks.get_items()] == ["Large Soda", "Iced Tea"]
    assert [item.get_name() for item in desserts.get_items()] == ["Chocolate Cookie"]
    assert [item.get_name() for item in drinks.filter_items()] == ["Large Soda", "Iced Tea"]

